# Canny Edge Detection
Canny is designed to improve on the results of sobel by:
1. Detect real edges
2. Be robust to noise
3. Produce thin, connected lines

Why do we care(some examples)?:
- Gather features of objects for object classification
- Extract vanishing points to assist in inferencing 3D information 
- lanes for autonomous cars, or safety features


It does this in 5 steps:

---

# 1. Gaussian Blur (Noise Reduction)
Before finding edges, we smooth the image.

- Why? Noise can look like fake edges.
- We apply a Gaussian filter (blurring).

Result: A smoother image with less noise.

---

# 2. Gradient (Edge Strength & Direction)
Now we find where intensity changes sharply.

- Compute gradients in x and y (using Sobel filters):
  - Gx, Gy

- Magnitude (edge strength):
  G = sqrt(Gx^2 + Gy^2)

- Direction (edge orientation):
  theta = arctan(Gy / Gx)

Result:
- Bright pixels = strong edges
- Direction tells which way the edge is pointing

---

# 3. Non-Maximum Suppression (NMS)
This step thins edges.

Problem: Gradients produce thick edges

Solution:
- For each pixel, look along the gradient direction
- Keep it only if it’s a local maximum
- Otherwise, suppress it (set to 0)

Result: Thin, 1-pixel-wide edges

---

# 4. Double Thresholding
Now we classify edges into strong, weak, or none.

- High threshold → strong edges
- Low threshold → weak edges
- Below low → discard

Result:
- Strong edges = definitely real
- Weak edges = maybe real

---

# 5. Edge Tracking by Hysteresis
This is the decision-making step.

- Keep weak edges only if connected to strong edges
- Remove weak edges that are isolated

Result: Clean, connected edges

