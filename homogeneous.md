## 1. Why homogeneous coordinates exist

In **2D or 3D Euclidean space**, we represent points as:
- 2D point: \((x, y)\)
- 3D point: \((x, y, z)\)

This works fine for **translations, rotations, and scaling**, but there’s a problem:

**Translation cannot be represented as a matrix multiplication** in standard coordinates.

For example:
$ (x, y) \rightarrow (x + t_x, y + t_y) $

This is not linear.

Homogeneous coordinates solve this by **adding one extra dimension**, allowing *all affine transformations* (translation, rotation, scaling, shear) to be done using **matrix multiplication**.

---

## 2. Basic idea

### 2D → Homogeneous 2D
A 2D point \((x, y)\) becomes:
$
(x, y, 1)
$

More generally:
$
(x, y) \equiv (kx, ky, k) \quad \text{for any } k \neq 0
$

So:
- \((2, 4, 2)\)
- \((1, 2, 1)\)
- \((0.5, 1, 0.5)\)

all represent the **same point** \((1, 2)\).

To convert back:
$
(x, y, w) \rightarrow \left(\frac{x}{w}, \frac{y}{w}\right)
$

---

### 3D → Homogeneous 3D
A 3D point \((x, y, z)\) becomes:
$
(x, y, z, 1)
$

And:
$
(x, y, z, w) \rightarrow \left(\frac{x}{w}, \frac{y}{w}, \frac{z}{w}\right)
$

---

## 3. Transformations using matrices

### Translation (2D example)

$$
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
=
\begin{bmatrix}
x + t_x \\
y + t_y \\
1
\end{bmatrix}
$$

Now translation **is** a matrix multiplication 

---

### Rotation + Translation (rigid transform)

$$
\begin{bmatrix}
\cos\theta & -\sin\theta & t_x \\
\sin\theta & \cos\theta & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

This single matrix does:
- rotation
- then translation

---

## 4. Points vs vectors (important!)

Homogeneous coordinates distinguish **points** and **direction vectors**:

- **Point**: \((x, y, 1)\)
- **Vector**: \((v_x, v_y, 0)\)

Why?
- Vectors should **not** move under translation.
- Points should.

Example:
$$
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
v_x \\
v_y \\
0
\end{bmatrix}
=
\begin{bmatrix}
v_x \\
v_y \\
0
\end{bmatrix}
$$

Perfect behavior.

---

## 5. Geometric interpretation

Homogeneous coordinates represent **projective space**:

- Points with \(w = 1\): normal points
- Points with \(w = 0\): **points at infinity** (directions)

This is why they’re powerful in:
- computer vision
- perspective projection
- camera models

Parallel lines intersect “at infinity” in homogeneous space.

---

## 6. Perspective projection (why graphics uses them)

In 3D graphics, after projection you get:
$
(x', y', z', w')
$

Then you do the **perspective divide**:
$
(x, y, z) = \left(\frac{x'}{w'}, \frac{y'}{w'}, \frac{z'}{w'}\right)
$

This allows:
- depth perception
- vanishing points
- realistic perspective

---

## 7. Summary

**Homogeneous coordinates:**
- Add one extra dimension
- Allow translation to be a matrix multiplication
- Unify all affine transformations
- Distinguish points (\(w=1\)) from vectors (\(w=0\))
- Enable perspective projection and points at infinity
