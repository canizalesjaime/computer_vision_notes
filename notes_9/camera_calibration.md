# Camera Calibration

## What Is Camera Calibration?

Camera calibration is the process of determining the mathematical model of a camera so that we can accurately relate points in the **real world** to points in an **image**.

A camera image is only a 2D projection of a 3D scene. Calibration helps us understand:

- how the camera forms images,
- the geometry of the camera,
- how the camera is positioned in space,
- and how the lens distorts the image.

Without calibration, measurements from images are often inaccurate.

---

# Why Camera Calibration Is Useful

Camera calibration is important in many fields:

- **Robotics** — robots need calibrated cameras for navigation, object detection, grasping, and localization.
- **Computer vision** — tasks like 3D reconstruction and pose estimation depend on accurate geometry.
- **Augmented reality (AR)** — virtual objects must align correctly with the real world.
- **Self-driving cars** — lane detection and depth estimation require calibrated cameras.
- **Measurement systems** — converting pixels into real-world distances requires calibration.
- **Stereo vision** — depth estimation between two cameras depends heavily on accurate calibration.

For example:

If a robot sees an object at pixel coordinates `(u,v)`, calibration allows the robot to estimate where that object exists in real 3D space.

---

# The Camera Projection Model

A camera transforms a 3D world point into a 2D image point.

A point in the world:

$$
P_w =\begin{bmatrix}
X \\ 
Y \\
Z \\
1 \end{bmatrix}
$$

is projected into image coordinates:

$$
p = \begin{bmatrix} 
u \\ 
v \\
1 \end{bmatrix}
$$

using the camera model.

The full projection equation is:

$$
s \begin{bmatrix}
u \\ 
v \\ 
1 
\end{bmatrix} = K \begin{bmatrix} R & t \end{bmatrix} 
\begin{bmatrix} 
X \\
Y \\
Z \\
1 \end{bmatrix}
$$

where:

- (s) = scaling factor
- (K) = intrinsic matrix
- (R) = rotation matrix
- (t) = translation vector

This equation combines:

1. **Extrinsic parameters**  
   (where the camera is located and how it is oriented)

2. **Intrinsic parameters**  
   (how the camera internally forms the image)

---

# Intrinsic Parameters

Intrinsic parameters describe the **internal properties of the camera**.

These parameters are independent of the camera’s position in the world.

They describe:

- focal length,
- pixel scaling,
- image center,
- and skew.

These values are stored in the **intrinsic matrix**:

$$
K = \begin{bmatrix} 
f_x & s & c_x \\ 
0 & f_y & c_y \\ 
0 & 0 & 1\end{bmatrix}
$$

---

# Meaning of Each Intrinsic Parameter

## ($f_x$) and ($f_y$) — Focal Lengths

These represent the focal length measured in **pixels**.

- $f_x$ controls scaling in the x-direction
- $f_y$ controls scaling in the y-direction

The focal length determines how “zoomed in” the camera appears.

Larger focal lengths:
- narrower field of view,
- more zoom.

Smaller focal lengths:
- wider field of view.

---

## $c_x$ and $c_y$ — Principal Point

These represent the image center (also called the principal point).

Ideally, the optical center is exactly in the middle of the image, but real cameras are slightly offset.

So:

- $c_x$ = x-coordinate of optical center
- $c_y$ = y-coordinate of optical center

---

## (s) — Skew Parameter

This describes whether the image axes are perfectly perpendicular.

Most modern cameras have: s = 0

because pixels are rectangular and aligned properly.

Older cameras or special imaging systems may have nonzero skew.

---

# Extrinsic Parameters

Extrinsic parameters describe the camera’s position and orientation in the world.

They answer:

- Where is the camera?
- Which direction is it facing?

The extrinsic parameters consist of:

$[R  |  t]$

where:

- (R) = rotation matrix
- (t) = translation vector

---

# Translation Vector (t)

The translation vector describes the camera’s position relative to the world coordinate system.

$$
t =\begin{bmatrix} t_x \\
 t_y \\
  t_z \end{bmatrix}
$$

It tells us how far the camera is shifted in:

- x direction,
- y direction,
- z direction.

---

# Rotation Matrix (R)

The rotation matrix describes the orientation of the camera.

It tells us how the camera is rotated relative to the world axes.

A 3D rotation can be represented using rotations about:

- x-axis,
- y-axis,
- z-axis.

These are often combined together to form the full rotation matrix.

---

# Rotation Around the X-Axis — $R_x$

Rotation about the x-axis changes:

- pitch,
- rotating sideways.

The matrix is:

$$
R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\
 0 & \cos\theta & -\sin\theta \\ 
 0 & \sin\theta & \cos\theta \end{bmatrix}
$$

Effect:
- x-coordinate stays unchanged
- y and z rotate together

This is like tilting your head sideways.

---

# Rotation Around the Y-Axis — $R_y$

Rotation about the y-axis changes:

- yaw,
- looking up/down.

The matrix is:

$$
R_y(\theta)=\begin{bmatrix} \cos\theta & 0 & \sin\theta \\
 0 & 1 & 0 \\
  -\sin\theta & 0 &\cos\theta \end{bmatrix}
$$

Effect:
- y-coordinate stays unchanged
- x and z rotate together

You can imagine tilting a camera upward or downward.

---

# Rotation Around the Z-Axis — \(R_z\)

Rotation about the z-axis changes:

- roll,
- looking left/right.

The matrix is:

$$
R_z(\theta)=\begin{bmatrix}\cos\theta & -\sin\theta & 0 \\
 \sin\theta & \cos\theta & 0 \\
  0 & 0 & 1 \end{bmatrix}
$$

Effect:
- z-coordinate stays unchanged
- x and y rotate together

This is like turning your head left or right.

---

# Combining Rotations

The final rotation matrix is often formed by multiplying these matrices:

$R = R_x R_y R_z$

The multiplication order matters because 3D rotations are not commutative.

Changing the order changes the final orientation.

---

# Lens Distortion

Real camera lenses are imperfect.

Because of this, straight lines in the real world may appear curved in the image.

This effect is called **distortion**.

There are two major types:

---

## Radial Distortion

Radial distortion causes bending near the edges of the image.

Common forms:

- **Barrel distortion**  
  image bulges outward

- **Pincushion distortion**  
  image pinches inward

Radial distortion is usually modeled with coefficients such as:

$k_1, k_2, k_3$

---

## Tangential Distortion

Tangential distortion happens when the lens is not perfectly aligned with the image sensor.

This causes the image to appear slightly tilted or stretched.

Tangential distortion is modeled using:

$p_1, p_2$

---

# Distortion Coefficients

A typical distortion coefficient vector looks like:

$[k_1, k_2, p_1, p_2, k_3]$

Calibration estimates these values so software can:

- remove distortion,
- straighten lines,
- improve geometric accuracy.

This process is called **image undistortion**.

---

# Full Camera Projection Equation

Putting everything together:

$$
s \begin{bmatrix} u \\
 v \\
  1 \end{bmatrix} = K \begin{bmatrix} R & t \end{bmatrix} \begin{bmatrix}X \\
   Y \\
    Z \\
     1 \end{bmatrix}
$$

This equation describes the entire imaging pipeline:

1. transform world coordinates into camera coordinates,
2. rotate and translate the scene,
3. project the 3D point onto the image plane,
4. apply camera intrinsics,
5. apply distortion corrections.

---

# High-Level Camera Calibration Process

A common calibration workflow looks like this:

---

## 1. Print a Checkerboard Pattern

A checkerboard is commonly used because its corner points are easy to detect accurately.

The square size should be known.

---

## 2. Take Multiple Images

Capture many images of the checkerboard:

- from different angles,
- different distances,
- different positions in the frame.

This gives the calibration algorithm enough geometric variation.

---

## 3. Detect Checkerboard Corners

Software detects the checkerboard corner points in each image.

Examples:
- OpenCV’s `findChessboardCorners()`
- Harris corner detection methods

These image points are matched with known real-world checkerboard coordinates.

---

## 4. Solve for Camera Parameters

The calibration algorithm estimates:

- intrinsic matrix K,
- rotation matrices R,
- translation vectors t,
- distortion coefficients.

The algorithm minimizes projection error between:
- predicted image points,
- actual detected points.

---

## 5. Evaluate Reprojection Error

After calibration, the software computes reprojection error.

Low error means:
- the camera model matches the real camera well.

---

## 6. Use the Calibration Results

The calibrated parameters can then be used for:

- pose estimation,
- 3D reconstruction,
- robotics,
- stereo vision,
- AR applications,
- image undistortion,
- measurement tasks.

