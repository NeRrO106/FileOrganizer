import os
import customtkinter as ctk
from tkinter import filedialog
from config import (
    BG, BG2, BG3, BORDER, TEXT, TEXT_DIM, GREEN, RED, BLUE,
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT,
    FONT_EMOJI, FONT_CODE, EXTENSII
)


class UIBuilder:

    def __init__(self, app, on_folder_change=None, on_run=None):
        self.app = app
        self.on_folder_change = on_folder_change or (lambda x: None)
        self.on_run = on_run or (lambda: None)

    def setup_window(self):
        self.app.title("Desktop Organizer")
        self.app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.app.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.app.configure(fg_color=BG)

    def build_header(self):
        header = ctk.CTkFrame(
            self.app, fg_color=BG2, corner_radius=0,
            height=64, border_width=1, border_color=BORDER
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(
            header, text="🗂️", font=(FONT_EMOJI, 28)
        ).pack(side="left", padx=(20, 8), pady=10)

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side="left", pady=10)
        ctk.CTkLabel(
            title_frame, text="Desktop Organizer",
            font=(FONT_CODE, 16, "bold"), text_color=TEXT
        ).pack(anchor="w")
        ctk.CTkLabel(
            title_frame, text="sortare automată după extensie",
            font=(FONT_CODE, 10), text_color=TEXT_DIM
        ).pack(anchor="w")

        self.status_label = ctk.CTkLabel(
            header, text="", font=(FONT_CODE, 11), text_color=GREEN
        )
        self.status_label.pack(side="right", padx=20)

        return self.status_label

    def build_folder_controls(self):
        folder_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        folder_frame.pack(fill="x", padx=20, pady=(16, 0))

        ctk.CTkLabel(
            folder_frame, text="FOLDER ȚINTĂ",
            font=(FONT_CODE, 10, "bold"), text_color=TEXT_DIM
        ).pack(anchor="w", pady=(0, 4))

        row = ctk.CTkFrame(folder_frame, fg_color="transparent")
        row.pack(fill="x")

        self.folder_var = ctk.StringVar(
            value=os.path.join(os.path.expanduser("~"), "Desktop")
        )
        self.folder_entry = ctk.CTkEntry(
            row, textvariable=self.folder_var,
            font=(FONT_CODE, 12), fg_color=BG2,
            border_color=BORDER, text_color=TEXT, height=38
        )
        self.folder_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        ctk.CTkButton(
            row, text="📂 Browse", width=100, height=38,
            font=(FONT_CODE, 12), fg_color=BG3,
            hover_color=BORDER, text_color=TEXT,
            border_width=1, border_color=BORDER,
            command=self._on_browse
        ).pack(side="left", padx=(0, 8))

        self.run_btn = ctk.CTkButton(
            row, text="▶  Rulează", width=110, height=38,
            font=(FONT_CODE, 13, "bold"),
            fg_color=BLUE, hover_color="#3b7de8",
            command=self.on_run
        )
        self.run_btn.pack(side="left")

        return self.folder_var, self.run_btn

    def build_progress_bar(self):
        pb_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        pb_frame.pack(fill="x", padx=20, pady=(12, 0))

        self.progress = ctk.CTkProgressBar(
            pb_frame, height=6, fg_color=BG2,
            progress_color=BLUE, corner_radius=3
        )
        self.progress.pack(fill="x")
        self.progress.set(0)

        self.progress_label = ctk.CTkLabel(
            pb_frame, text="",
            font=(FONT_CODE, 10), text_color=TEXT_DIM
        )
        self.progress_label.pack(anchor="w", pady=(3, 0))

        return self.progress, self.progress_label

    def build_tabs(self):
        self.tabview = ctk.CTkTabview(
            self.app, fg_color=BG2,
            segmented_button_fg_color=BG3,
            segmented_button_selected_color=BG,
            segmented_button_selected_hover_color=BG,
            segmented_button_unselected_color=BG3,
            segmented_button_unselected_hover_color=BORDER,
            text_color=TEXT, border_width=1, border_color=BORDER,
            corner_radius=10
        )
        self.tabview.pack(fill="both", expand=True, padx=20, pady=12)

        self.tabview.add("📁  Fișiere")
        self.tabview.add("🏷️  Categorii")
        self.tabview.add("📋  Log")

        return self.tabview

    def build_files_tab(self):
        tab = self.tabview.tab("📁  Fișiere")
        tab.configure(fg_color="transparent")

        self.files_scroll = ctk.CTkScrollableFrame(
            tab, fg_color="transparent",
            scrollbar_button_color=BORDER,
            scrollbar_button_hover_color=TEXT_DIM
        )
        self.files_scroll.pack(fill="both", expand=True)

        return self.files_scroll

    def refresh_files_tab(self, files_data):
        for w in self.files_scroll.winfo_children():
            w.destroy()

        if files_data is None:
            ctk.CTkLabel(
                self.files_scroll, text="⚠️  Folderul nu există.",
                font=(FONT_CODE, 12), text_color=RED
            ).pack(pady=20)
            return

        if not files_data:
            ctk.CTkLabel(
                self.files_scroll, text="📭  Folderul este gol.",
                font=(FONT_CODE, 12), text_color=TEXT_DIM
            ).pack(pady=20)
            return

        for filename, (cat_name, cat_color, cat_icon) in files_data.items():
            self._file_row(self.files_scroll, filename, cat_name, cat_color, cat_icon)

    def _file_row(self, parent, filename, cat_name, cat_color, cat_icon):
        row = ctk.CTkFrame(parent, fg_color=BG3, corner_radius=8, height=38)
        row.pack(fill="x", pady=2)
        row.pack_propagate(False)

        ctk.CTkFrame(row, fg_color=cat_color, width=3, corner_radius=0).pack(
            side="left", fill="y", padx=(0, 10)
        )

        ctk.CTkLabel(
            row, text=cat_icon, font=(FONT_EMOJI, 15), width=24
        ).pack(side="left", padx=(0, 8))

        ctk.CTkLabel(
            row, text=filename, font=(FONT_CODE, 11),
            text_color=TEXT, anchor="w"
        ).pack(side="left", fill="x", expand=True)

        if cat_name:
            category_text = cat_name.replace("_", " ")
        else:
            category_text = "necunoscut"

        ctk.CTkLabel(
            row, text=category_text,
            font=(FONT_CODE, 10), text_color=cat_color,
            width=100, anchor="e"
        ).pack(side="right", padx=10)

    def build_categories_tab(self):
        tab = self.tabview.tab("🏷️  Categorii")
        tab.configure(fg_color="transparent")

        scroll = ctk.CTkScrollableFrame(
            tab, fg_color="transparent",
            scrollbar_button_color=BORDER
        )
        scroll.pack(fill="both", expand=True)
        scroll.columnconfigure((0, 1), weight=1)

        for i, (name, data) in enumerate(EXTENSII.items()):
            card = ctk.CTkFrame(
                scroll, fg_color=BG3, corner_radius=10,
                border_width=1, border_color=data["color"]
            )
            card.grid(row=i // 2, column=i % 2, padx=6, pady=6, sticky="nsew")

            ctk.CTkLabel(
                card, text=data["icon"], font=(FONT_EMOJI, 22)
            ).pack(side="left", padx=(14, 10), pady=10)

            info = ctk.CTkFrame(card, fg_color="transparent")
            info.pack(side="left", fill="x", expand=True, pady=8)

            ctk.CTkLabel(
                info, text=name.replace("_", " "),
                font=(FONT_CODE, 12, "bold"), text_color=TEXT, anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info, text="  ".join(data["exts"]),
                font=(FONT_CODE, 9), text_color=TEXT_DIM, anchor="w"
            ).pack(anchor="w")

    def build_log_tab(self):
        tab = self.tabview.tab("📋  Log")
        tab.configure(fg_color="transparent")

        self.log_box = ctk.CTkTextbox(
            tab, font=(FONT_CODE, 11), fg_color=BG3,
            text_color=TEXT, border_width=1, border_color=BORDER,
            corner_radius=8, wrap="none"
        )
        self.log_box.pack(fill="both", expand=True)
        self.log_box.configure(state="disabled")

        return self.log_box

    def log(self, msg):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", msg + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def clear_log(self):
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

    def set_progress(self, value, label=""):
        self.progress.set(value)
        self.progress_label.configure(text=label)

    def set_status(self, text):
        self.status_label.configure(text=text)

    def set_run_button_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        text = "▶  Rulează" if enabled else "Se sortează..."
        self.run_btn.configure(state=state, text=text)

    def _on_browse(self):
        path = filedialog.askdirectory(initialdir=self.folder_var.get())
        if path:
            self.folder_var.set(path)
            self.on_folder_change(path)