import os
import threading
import customtkinter as ctk
from ui import UIBuilder
from organizer import FileOrganizer
from config import BG


class OrganizerApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.configure(fg_color=BG)

        self.ui = UIBuilder(
            self, on_folder_change=self._on_folder_change, on_run=self._start
        )

        self.organizer = FileOrganizer(
            on_log=self.ui.log,
            on_progress=self.ui.set_progress,
            on_status=self.ui.set_status,
        )

        self._build_ui()

    def _build_ui(self):
        self.ui.setup_window()
        self.ui.build_header()
        self.folder_var, self.run_btn = self.ui.build_folder_controls()
        self.ui.build_progress_bar()
        self.ui.build_tabs()
        self.ui.build_files_tab()
        self.ui.build_categories_tab()
        self.ui.build_log_tab()

        self._refresh_files()

    def _on_folder_change(self, folder_path):
        self._refresh_files()

    def _refresh_files(self):
        folder = self.folder_var.get()

        if not os.path.isdir(folder):
            self.ui.refresh_files_tab(None)
            return

        files = self.organizer.get_files_in_folder(folder)

        if not files:
            self.ui.refresh_files_tab({})
            return

        files_data = {}
        for filename in files:
            cat_name, cat_color, cat_icon = self.organizer.get_category(filename)
            files_data[filename] = (cat_name, cat_color, cat_icon)

        self.ui.refresh_files_tab(files_data)

    def _start(self):
        self.ui.set_run_button_enabled(False)
        self.ui.set_progress(0)
        self.ui.clear_log()
        self.ui.set_status("")

        threading.Thread(target=self._run_sort, daemon=True).start()

    def _run_sort(self):
        folder = self.folder_var.get()

        if not os.path.isdir(folder):
            self.ui.log(f"✗ Folderul nu există: {folder}")
            self.after(0, lambda: self.ui.set_run_button_enabled(True))
            return

        self.organizer.organize(folder)

        self.after(0, self._refresh_files)
        self.after(0, lambda: self.ui.set_run_button_enabled(True))


if __name__ == "__main__":
    app = OrganizerApp()
    app.mainloop()