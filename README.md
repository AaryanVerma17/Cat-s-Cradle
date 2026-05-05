# 🐱 Cat's Cradle - Neon Hand Tracking

> A real-time, futuristic string simulation powered by MediaPipe Hands and Canvas 2D. Point your hands at the camera and watch glowing laser strings weave between your fingertips.

---

## ✨ Features

- **Real-time hand tracking** - Detects up to 2 hands simultaneously using Google's MediaPipe Hands model
- **Neon laser strings** - Dynamic glowing strings connect matching fingertips (thumb↔thumb, index↔index, etc.)
- **Color-shifting strings** - Strings shift from **cyan → magenta → yellow** as hands move further apart
- **Particle explosions** - Touch fingertip-to-fingertip to trigger a burst of neon particles
- **Hand silhouettes** - Skeleton joints and bones drawn in cyan (left) and magenta (right)
- **CRT scanline overlay** - Retro-futuristic scanline animation for that deep synthwave aesthetic
- **HUD display** — Live tracking status, hand count, and particle count
- **Single file** — Zero build step, zero dependencies to install. Just one `.html` file

---
## 🎮 How to Use

| Action | Effect |
|---|---|
| Hold up one hand | Neon skeleton + strings from fingertips to palm |
| Hold up both hands | Laser strings connect matching fingertips |
| Move hands apart | Strings shift color and thin out |
| Touch fingertip to fingertip | 💥 Particle explosion |

---

## 🧰 Tech Stack

| Library | Purpose |
|---|---|
| [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) | Real-time hand landmark detection (21 points per hand) |
| [MediaPipe Camera Utils](https://www.npmjs.com/package/@mediapipe/camera_utils) | WebRTC camera feed management |
| HTML5 Canvas 2D | Rendering — glow effects via `shadowBlur`, particles, laser beams |
| Vanilla JavaScript | All animation and interaction logic |

All libraries are loaded via CDN — no `npm install` required.

---

## 📁 Project Structure

```
cats-cradle/
└── index.html    # Entire app — HTML + CSS + JS in one file
└── README.md     # This file
```

---
🔗 Live Demo
[View on Render](https://cat-s-cradle-dglf.onrender.com)