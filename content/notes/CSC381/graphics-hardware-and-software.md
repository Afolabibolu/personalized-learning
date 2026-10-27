# Graphics Hardware and Software

## Display devices

- A **raster-scan display** sweeps the screen row by row, lighting pixels from an image stored in the **frame buffer** (refresh buffer). Modern LCD, LED and OLED monitors are raster devices.
- A **random-scan (vector) display** draws lines directly between points. It gives smooth lines but cannot fill areas well, and is now rare.

**Key terms:**

- **Resolution:** the number of pixels across and down, such as 1920 × 1080.
- **Colour depth (bits per pixel):** 24 bits gives about 16.7 million colours.
- **Frame buffer size** = width × height × bits per pixel ÷ 8 bytes. A 1920 × 1080 screen at 24 bits needs about 6.2 MB.
- **Refresh rate:** how many times per second the image is redrawn, such as 60 or 144 Hz.
- **Aspect ratio:** width to height, such as 16:9.

## The GPU and the graphics pipeline

The **graphics processing unit (GPU)** is a highly parallel processor that renders images. Data passes through the **graphics pipeline**:

1. vertex processing (transformations);
2. primitive assembly;
3. **rasterisation** (turning primitives into fragments);
4. fragment or pixel shading;
5. writing to the frame buffer.

Its own fast memory (**VRAM**) holds textures and frame buffers.

## Choosing hardware for a design studio

- **CPU:** many fast cores, for rendering, simulation and multitasking.
- **RAM:** plenty, 32 GB or more, for large images, 3D scenes and video.
- **Storage:** fast **SSD** (NVMe) for the system and working files, with large HDDs or network storage and backups for archives.
- **Graphics card:** a powerful GPU with ample VRAM for 3D, video and real-time viewport performance.
- **Monitor:** high resolution, accurate colour (wide gamut such as Adobe RGB, calibrated), and IPS panels.
- **Input devices:** graphics tablets and styluses.

## Graphics software

- **Graphics APIs** give programs access to the GPU: **OpenGL**, **Vulkan**, **Direct3D** and **WebGL**.
- **Design software:** raster editors (Photoshop, GIMP), vector editors (Illustrator, Inkscape), 3D modelling and animation (Blender, Maya) and CAD (AutoCAD).

## Collaborative software for design teams

A design agency can improve communication and productivity with:

- **project management software** (Trello, Asana, Jira) to assign tasks, track deadlines and review status;
- **file-sharing software** (Google Drive, Dropbox, OneDrive) with version history and permissions;
- **design software with real-time collaboration** (Figma, Canva, Adobe Creative Cloud libraries), where several people edit and comment on the same file at once;
- **communication tools** (Slack, Microsoft Teams, Zoom).



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
