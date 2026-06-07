import os
import shutil
from config import EXTENSII


class FileOrganizer:

    def __init__(self, on_log, on_progress, on_status):
        self.on_log = on_log
        self.on_progress = on_progress
        self.on_status = on_status

    def get_category(self, filename):
        ext = os.path.splitext(filename)[1].lower()

        for category_name, category_data in EXTENSII.items():
            if ext in category_data["exts"]:
                return (
                    category_name,
                    category_data["color"],
                    category_data["icon"]
                )

        return (None, "#64748b", "❓")

    def get_files_in_folder(self, folder):
        if not os.path.isdir(folder):
            return None

        try:
            files = [
                f for f in os.listdir(folder)
                if os.path.isfile(os.path.join(folder, f))
            ]
            return sorted(files)
        except Exception as e:
            self.on_log(f"✗ Eroare la citire folder: {e}")
            return []

    def organize(self, folder):
        if not os.path.isdir(folder):
            self.on_log(f"✗ Folderul nu există: {folder}")
            return

        files = self.get_files_in_folder(folder)
        if files is None:
            self.on_log(f"✗ Folderul nu există: {folder}")
            return

        total = len(files)
        moved = 0
        errors = 0

        for i, fisier in enumerate(files):
            _, ext = os.path.splitext(fisier)
            category, _, _ = self.get_category(fisier)

            if category:
                destinatie = os.path.join(folder, category)
                os.makedirs(destinatie, exist_ok=True)

                try:
                    source = os.path.join(folder, fisier)
                    dest = os.path.join(destinatie, fisier)
                    shutil.move(source, dest)
                    moved += 1
                    msg = f"✓  {fisier}  →  {category}"
                    self.on_log(msg)
                except PermissionError:
                    errors += 1
                    msg = f"✗  {fisier}  →  folosit în alt program"
                    self.on_log(msg)
                except Exception as e:
                    errors += 1
                    msg = f"✗  {fisier}  →  {str(e)}"
                    self.on_log(msg)
            elif ext:
                msg = f"–  {fisier}  →  extensie necunoscută ({ext})"
                self.on_log(msg)

            progress_val = (i + 1) / total if total else 1
            label_text = f"{i + 1} / {total} fișiere procesate"
            self.on_progress(progress_val, label_text)

        summary = f"✅  Gata — {moved} mutate, {errors} erori"
        self.on_log("\n" + summary)
        self.on_status(f"✓ {moved} mutate · {errors} erori")

        return moved, errors