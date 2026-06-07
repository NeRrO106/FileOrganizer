import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

EXTENSII = {
    "Imagini": {
        "exts": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".webp", ".jfif", ".avif"],
        "icon": "🖼️",
        "color": "#f59e42"
    },
    "Documente": {
        "exts": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".accdb", ".csv", ".pptx", ".md"],
        "icon": "📄",
        "color": "#4f8ef7"
    },
    "Baze_De_Date": {
        "exts": [".db", ".sqlite", ".sqlite3"],
        "icon": "🗄️",
        "color": "#a78bfa"
    },
    "Video": {
        "exts": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "icon": "🎬",
        "color": "#f43f5e"
    },
    "Music": {
        "exts": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "icon": "🎵",
        "color": "#10b981"
    },
    "Arhive": {
        "exts": [".rar", ".zip", ".7z", ".tar", ".gz", ".xz"],
        "icon": "📦",
        "color": "#f97316"
    },
    "Executabile": {
        "exts": [".exe", ".msi", ".bat", ".cmd"],
        "icon": "⚙️",
        "color": "#64748b"
    },
}

BG = "#0f172a"           # Fundal principal
BG2 = "#1e293b"          # Fundal secundar (headers, tabs)
BG3 = "#273449"          # Fundal terțiar (inputs, frames)
BORDER = "#334155"       # Culoare borduri
TEXT = "#e2e8f0"         # Text principal
TEXT_DIM = "#64748b"     # Text secondary/dim
GREEN = "#22c55e"        # Verde (success)
RED = "#f43f5e"          # Roșu (errors)
BLUE = "#4f8ef7"         # Albastru (primary)

WINDOW_WIDTH = 780
WINDOW_HEIGHT = 620
WINDOW_MIN_WIDTH = 680
WINDOW_MIN_HEIGHT = 520

FONT_EMOJI = "Segoe UI Emoji"
FONT_CODE = "Consolas"