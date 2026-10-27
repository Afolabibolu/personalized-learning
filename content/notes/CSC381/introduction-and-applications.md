# Introduction and Applications of Computer Graphics

## What computer graphics is

**Computer graphics** is the creation, storage and manipulation of pictures and models by computer. Images are held in two forms:

- **Raster (bitmap) images** are grids of **pixels**, each with a colour. They suit photographs, but lose quality when enlarged.
- **Vector images** are described by geometric primitives (lines, curves, polygons) and scale without loss. They suit drawings and fonts.

**Interactive graphics** lets the user control the image in real time, as in games and CAD. **Non-interactive (passive) graphics** produces images without user control, such as a printed chart or a pre-rendered film.

## Applications

- **Computer-aided design (CAD):** engineering parts, buildings and circuits.
- **Entertainment:** films, special effects, animation and games.
- **Visualisation:** scientific, medical (CT and MRI) and business data shown as images and charts.
- **Education and training:** simulators for flight, driving and surgery.
- **User interfaces:** windows, icons and menus.
- **Geographic information systems (GIS)** and mapping.
- **Image processing**, which works the other way, analysing existing images.

## Graphics in autonomous robots

Computer graphics supports autonomous robots in three main ways:

- **Simulation:** robots are tested in virtual 3D worlds (simulators such as Gazebo) before risking real hardware. Their sensors and physics are modelled, which is cheaper and safer, and rare dangerous situations can be generated.
- **Sensor data processing:** camera images, LiDAR point clouds and depth maps are turned into 3D models of the surroundings by reconstruction and mapping (SLAM: simultaneous localisation and mapping).
- **Decision-making:** the reconstructed scene, drawn as maps and occupancy grids, lets the robot plan paths, recognise objects and avoid obstacles, and lets operators see what the robot "sees".

## Building detection and mapping from aerial images

Automatic detection of buildings from aerial or satellite images combines graphics, image processing and computational geometry:

1. **Pre-processing:** correct the geometry (orthorectification), reduce noise and enhance contrast.
2. **Feature extraction:** detect edges (Canny, Sobel) and corners, and find straight lines with the **Hough transform**, since building outlines are mostly straight.
3. **Segmentation and classification:** group pixels into regions by colour, texture and height (from LiDAR or stereo images), often with machine learning such as convolutional neural networks.
4. **Shape regularisation:** fit polygons to detected outlines and simplify them into right-angled footprints.
5. **Mapping:** convert footprints to vector maps in a GIS, and build 3D city models from heights.



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
