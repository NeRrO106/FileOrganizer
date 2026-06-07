# Desktop Organizer - Structura Proiectului

## 📁 Organizare Fișiere

```
organizer/
├── main.py          # Punct de intrare - orchestrează aplicația
├── config.py        # Configurații, culori, constante
├── ui.py            # Interfața grafică (componente și layout)
├── organizer.py     # Logica de sortare și mutare de fișiere
└── README.md        # Acest fișier
```

## 📝 Descriere Fișiere

### `main.py` - Aplicația Principală
- **Responsabilitate**: Orchestrează UI-ul și logica
- **Clasa**: `OrganizerApp` (extinde `ctk.CTk`)
- **De modificat cand**: Vrei să schimbi fluxul aplicației, cum se inițiază sau cum se comunică componentele

```python
if __name__ == "__main__":
    app = OrganizerApp()
    app.mainloop()
```

### `config.py` - Configurații
- **Responsabilitate**: Definește toate constantele
- **Conține**:
  - Extensii de fișiere și categorii
  - Culori (tema dark)
  - Dimensiuni fereastră
  - Fonturi
  
- **De modificat cand**: 
  - Vrei să adaugi/modifici categorii
  - Schimbi culorile temei
  - Schimbi dimensiuni fereastră

```python
# Exemplu: Adaugă o categorie nouă
EXTENSII["Cod_Sursa"] = {
    "exts": [".py", ".js", ".cpp", ".java"],
    "icon": "💻",
    "color": "#06b6d4"
}
```

### `ui.py` - Interfața Grafică
- **Responsabilitate**: Construiește și gestionează UI
- **Clasa**: `UIBuilder`
- **Metode principale**:
  - `build_header()` - Construiește header-ul
  - `build_folder_controls()` - Controale folder
  - `build_tabs()` - Construiește tab-urile
  - `refresh_files_tab()` - Reîmprospătează lista fișiere
  - `log()` - Adaugă mesaje în log
  
- **De modificat cand**:
  - Vrei să schimbi design-ul interfaței
  - Adaugi noi controale
  - Schimbi dispunerea componentelor

### `organizer.py` - Logica de Sortare
- **Responsabilitate**: Sortează și mută fișierele
- **Clasa**: `FileOrganizer`
- **Metode principale**:
  - `get_category(filename)` - Determină categoria unui fișier
  - `get_files_in_folder(folder)` - Listează fișierele
  - `organize(folder)` - Execută sortarea
  
- **De modificat cand**:
  - Vrei să schimbi logica de sortare
  - Adaugi validări suplimentare
  - Schimbi comportamentul la erori

## 🚀 Cum să Rulezi

```bash
python main.py
```

## 🔧 Exemple de Modificări

### Adaugă o categorie nouă
```python
# În config.py
EXTENSII["Proiecte"] = {
    "exts": [".sln", ".vcxproj", ".proj"],
    "icon": "🔧",
    "color": "#8b5cf6"
}
```

### Schimbă culoarea temei
```python
# În config.py
BLUE = "#06b6d4"  # Din albastru în cyan
RED = "#ff6b6b"   # Din roșu în roșu mai vibrant
```

### Adaugă o nouă funcție de organizare
```python
# În organizer.py
def organize_by_date(self, folder):
    """Organizează fișierele după data modificării"""
    # Implementare...
```

### Personalizează mesajele din log
```python
# În organizer.py, metoda organize()
msg = f"✓  {fisier}  →  {category}"  # Schimbă emoticons sau format
```

## 📊 Flux de Execuție

```
1. main.py inițiază OrganizerApp
2. OrganizerApp apelează UIBuilder.build_ui()
3. UIBuilder construiește toate componentele
4. User selectează folder și apasă "Rulează"
5. OrganizerApp._start() apelează organize()
6. FileOrganizer.organize() execută sortarea în thread separat
7. Mesajele sunt trimise via callbacks la UI
8. UI se actualizează în real-time
```

## 💡 Sfaturi pentru Debugging

- **Log messages**: Verifică tab-ul "Log" pentru mesaje detaliate
- **Test cu folder mic**: Folosește un folder de test cu câțiva fișiere
- **Print statements**: Adaugă print() în `organizer.py` pentru debugging logicii
- **UI freezing**: Sortarea se execută în thread separat pentru a nu bloca UI

## 📦 Dependențe

```bash
pip install customtkinter
```

## 🎨 Personalizare Ușoară

Cea mai ușor de personalizat este `config.py`:
- Schimbă culori
- Adaugă/modifica categorii
- Schimbă dimensiuni fereastră
- Adaugă emoji-uri noi

Toate celelalte fișiere folosesc aceste constante!

---

**Versiune**: 1.0  
**Limbă**: Română  
**Ultima actualizare**: 2024
