# 🔥 QR Code Generator Pro

A terminal-based Python application to generate customizable QR Codes — perfect for URLs, text, contact info, or any data you need to share via scan.

---

## 🚀 Features

- ✅ Generate standard QR Code (black & white)
- ✅ Generate custom QR Code with configurable colors
- ✅ Adjustable box size for QR code resolution
- ✅ Automatic `.png` extension handling
- ✅ Input validation with error handling
- ✅ Clean menu-driven interface

---

## 📸 Preview

```
========================================
      🔥 QR CODE GENERATOR PRO 🔥      
========================================
1. Generate QR Code (Standard)
2. Customize QR Code (Color & Size)
3. Exit
========================================
Choose menu (1-3): 2

--- 2. GENERATE CUSTOM QR CODE ---
Enter URL or text: https://github.com/aryawirawicaksana029-ui

[Size Settings]
Enter box size (Recommended: 10): 10

[Color Settings] (Use English color names, e.g., black, white, red, blue)
QR Code Color (Default: black): red
Background Color (Default: white): black

Enter output filename (example: custom_qr): my_github_qr
⏳ Building your custom QR Code...
🎨 Awesome! Custom QR Code saved as: my_github_qr.png
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| QR Generation | qrcode library |
| Image Processing | Pillow (PIL) |
| Interface | Terminal / Command Line |

---

## ⚙️ How to Use

**1. Clone this repository:**
```bash
git clone https://github.com/aryawirawicaksana029-ui/qr-code-generator.git
cd qr-code-generator
```

**2. Install dependencies:**
```bash
pip install qrcode[pil]
```

**3. Run the program:**
```bash
python main_qr.py
```

**4. Choose an option:**
```
1 → Generate standard black & white QR code
2 → Generate custom QR code with colors and custom size
3 → Exit
```

---

## 🎨 Customization Options

| Option | Description | Default |
|--------|-------------|---------|
| Box Size | Pixel size per QR module | 10 |
| QR Color | Foreground color (English names) | black |
| Background Color | Background color (English names) | white |

---

## 📊 Use Cases

QR Codes generated can be used for:
- Website links
- WhatsApp links (wa.me/...)
- Plain text messages
- Email addresses
- Social media profiles
- Contact information

---

## 📁 Project Structure

```
qr-code-generator/
│
├── main_qr.py      # Main program with QR generation logic
└── README.md       # Project documentation
```

---

## 👨‍💻 Author

**Arya Wira Wicaksana**
🐍 Python Developer | AI Enthusiast
📧 aryawirawicaksana029@gmail.com
🔗 [GitHub](https://github.com/aryawirawicaksana029-ui)

---

## 🔮 Future Plans

- [ ] GUI version with Tkinter
- [ ] Web App version with Flask
- [ ] Logo embedding in QR code center
- [ ] Batch QR generation from CSV file
- [ ] QR code scanner/reader feature
- [ ] Support for vCard and WiFi QR codes
