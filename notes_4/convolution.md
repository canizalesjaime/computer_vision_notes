# Intro
Convolution is a mathematical operation that combines two functions (or signals) to show how one modifies or “blends with” the other over time or space. It shows up everywhere: signal processing, image filtering, probability, and neural networks.

## Convolution in images

In images, convolution is how filters work:
* Blur → average neighbors
* Sharpen → emphasize differences
* Edge detection → highlight intensity changes
* Each pixel becomes a weighted sum of nearby pixels.

## Convolution in neural networks (CNNs)

In deep learning, convolution layers:
* Slide small weight matrices (kernels) across data
* Detect patterns (edges → textures → objects)
* Key idea: shared weights + local patterns
* During training neural network solves for the filters 

## Key properties
* Commutative → f∗g=g∗f
* Associative → f∗(g∗h)=(f∗g)∗h
* Linear
* Convolution in time ↔ multiplication in frequency(Linear Shift-Invariant System)

## Convolution example (1D Case)
Convolution in images means:

Take a small filter (kernel), place it over the image, multiply overlapping pixels, sum them, move one pixel to the right, and repeat.

We will compute:

f = [1 2 3 4]     (image row)
g = [1 2]         (kernel)

Think of g as a tiny filter that:
- multiplies the left pixel by 1
- multiplies the right pixel by 2
- adds the results


## Output Size

For full discrete convolution:

len(f * g) = len(f) + len(g) - 1

So:

4 + 2 - 1 = 5

Output indices:

n = 0,1,2,3,4


## Convolution Formula

The discrete convolution formula is:

(f * g)[n] = Σ f[k] g[n-k]

Valid k must satisfy(for each value of n):

max(0,n-(L-1)) ≤ k ≤ min(M-1,n) where L=length of g, and M = length of f


## Image Sliding Interpretation
We now slide the kernel across the image.


Position n = 0
```
f:   [1  2  3  4]
g:[2  1]
```
Only overlap:

1 * 1 = 1

Output[0] = 1

---

Position n = 1
```
f:  [1  2  3  4]
g:  [2  1]
```
Compute:

1*2 + 2*1 = 2 + 2 = 4

Output[1] = 4

---

Position n = 2
```
f:  [1  2  3  4]
g:     [2  1]    
```
Compute:

2*2 + 3*1 = 4 + 3 = 7

Output[2] = 7

---

Position n = 3

```
f:  [1  2  3  4]
g:        [2  1]
```
Compute:

3*2 + 4*1 = 6 + 4 = 10

Output[3] = 10
---

Position n = 4
```
f:  [1  2  3  4]
g:           [2  1]
```
Only overlap:

4 * 2 = 8

Output[4] = 8


## Algebraic Solution Using the Formula

We compute using:

(f * g)[n] = Σ f[k] g[n-k]

with max(0,n-(L-1)) ≤ k ≤ min(M-1,n) where L=length of g, and M = length of f

n = 0

k = 0

(f * g)[0] = f[0]g[0] = 1*1 = 1

---

n = 1

k = 0,1

(f * g)[1] = f[0]g[1] + f[1]g[0]
          = 1*2 + 2*1
          = 4

---

n = 2

k = 1,2

(f * g)[2] = f[1]g[1] + f[2]g[0]
          = 2*2 + 3*1
          = 7

---

n = 3

k = 2,3

(f * g)[3] = f[2]g[1] + f[3]g[0]
          = 3*2 + 4*1
          = 10

---

n = 4

k = 3

(f * g)[4] = f[3]g[1]
          = 4*2
          = 8

---

Final Convolution Result

[1 4 7 10 8]


### Key Takeaways
- Output size = L + M − 1 (n={0,1,2,3,4})
- Valid k range: max(0,n-(L-1)) ≤ k ≤ min(M-1,n) where L=length of g, and M = length of f
- Convolution in images = sliding weighted sum
- The algebraic formula exactly matches the visual sliding process


## Box Filter (Mean / Averaging Filter)
A box filter replaces each pixel with the average of its neighbors.

For a 3×3 box filter:
```
B = (1/9) *
[
 [1 1 1]
 [1 1 1]
 [1 1 1]
]
```
All weights are equal.


### What It Does

For each pixel:

O[i,j] = (1/9) * sum of 3x3 neighborhood values

So it computes a simple average.


### Intuition

It treats all nearby pixels equally.

If a pixel has value 1 and its neighbors are 0, the output becomes:

(1/9) * 1 = 0.111...

So sharp edges become blurred quickly.


### Properties

- Linear
- Shift-invariant
- Fast to compute
- Produces noticeable blur
- Can create blocky artifacts


## Gaussian Filter
A Gaussian filter uses weighted averaging, where closer pixels matter more.

3×3 Gaussian: σ (approximately 1)
```
G = (1/16) *
[
 [1 2 1]
 [2 4 2]
 [1 2 1]
]
```
Notice:

- Center weight = 4
- Immediate neighbors = 2
- Corners = 1


### Where It Comes From

It approximates the continuous Gaussian function:

G(x,y) = exp(-(x^2 + y^2) / (2σ^2))

This produces a bell-shaped surface.


### What It Does

Each output pixel:

O[i,j] = sum over m,n of I[i-m,j-n] * G[m,n]

Unlike the box filter:

- Nearby pixels have higher influence
- Distant pixels have smaller influence


### Intuition

Think of it as a soft blur.

Instead of equal averaging, it does:

"Weight nearby pixels more heavily, because they are more related."

So edges blur more naturally and smoothly.


## Visual Comparison and Mathematical Differences

Suppose you have a sharp square of 1s in 0s.

### Box filter result:
- Edges become blurry quickly
- Interior drops slightly near edges
- Looks somewhat artificial

### Gaussian filter result:
- Edges soften gradually
- Interior preserved better
- More natural-looking blur

### Box Filter
- Equal weights
- Moderate smoothing
- Poor frequency behavior (ripples)

## Gaussian Filter
- Bell-shaped weights
- Very smooth
- Smooth frequency response
- No ringing artifacts

Both are:
- Linear
- Shift-invariant
- Low-pass filters (remove high frequencies)

### When to Use Which?

#### Use box filter when:
- You need something very fast
- Quality is not critical

#### Use Gaussian filter when:
- You want natural smoothing
- You want to reduce noise before edge detection
- You are doing computer vision

## Advantage of Using Different Size Filters for Box and Gaussian

Excellent question — filter size is actually more important than most people realize.

Changing the size changes how much smoothing happens and what frequencies get removed.


### What Does “Filter Size” Control?

If you increase filter size:

- You include more neighboring pixels
- You average over a larger area
- You remove more high frequencies
- You blur more

So filter size directly controls:

The spatial scale of smoothing

Small filter → small-scale smoothing  
Large filter → large-scale smoothing  

---

### Box Filter: Effect of Size

#### 3×3 Box
- Mild blur
- Removes small noise
- Edges still somewhat visible

#### 7×7 Box
- Strong blur
- Edges become soft quickly
- Small details disappear

#### Mathematical effect

For an N×N box filter:

Each pixel becomes:

1/N² × sum of N×N neighborhood

As N increases:
- Each individual pixel has less influence
- Image becomes flatter
- Edges smear more aggressively

---

### Gaussian Filter: Effect of Size

Gaussian has an additional parameter:

σ (sigma) = standard deviation

Filter size and sigma are related but not identical.

#### Larger Gaussian kernel:
- Covers more area
- Uses a larger σ
- Produces smoother, more natural blur

#### Key difference from box:
Even when large, Gaussian:
- Still weights center more heavily
- Doesn’t produce harsh averaging artifacts

---

## Why Use Different Sizes?

Because different problems require different smoothing scales.

## Example 1: Noise Removal

Small random noise?
- 3×3 Gaussian is enough

Heavy noise?
- 7×7 or 11×11 Gaussian

---

## Example 2: Preprocessing Before Edge Detection

If you use Sobel:

- Too small Gaussian → noisy edges
- Too large Gaussian → edges disappear

So size controls edge sensitivity.

---

## Example 3: Multi-Scale Vision (Very Important Concept)

In computer vision, objects exist at different scales.

Small filters detect:
- Fine texture
- Small details

Large filters detect:
- Big structures
- Coarse features

This is the idea behind:
- Scale-space theory
- Gaussian pyramids
- Multi-scale feature detection

---



### Tradeoffs of Larger Filters

### Pros
- Better noise removal
- Smoother results
- More global averaging

### Cons
- Loss of detail
- Blurred edges
- Higher computational cost

---

### Computational Cost Difference

For N×N kernel:

Direct convolution cost:

O(N² per pixel)

Large 21×21 filter becomes expensive.

But Gaussian has a huge advantage:

It is separable.

2D Gaussian convolution =
1D horizontal convolution +
1D vertical convolution

Cost becomes:

O(2N per pixel)

This is why large Gaussian filters are practical.

---

### Practical Rule of Thumb

If you want:

- Light smoothing → 3×3 or 5×5
- Moderate smoothing → 7×7
- Heavy blur → 11×11 or larger
- Professional vision pipeline → tune sigma, not just size

---

### Filter size conclusion

Filter size controls:

How far information spreads in the image.

Small filter:
→ local smoothing

Large filter:
→ global smoothing

Box filter:
Spreads influence evenly.

Gaussian filter:
Spreads influence smoothly and naturally.

## Try 2d convolution with horizontal sobel filter for:
 ```
 [
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,1,1,1,1,0,0],
 [0,0,1,1,1,1,0,0],
 [0,0,1,1,1,1,0,0],
 [0,0,1,1,1,1,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0]
]
```

**horizontal sobel filter(used to detect vertical lines(dumb name))**
```
Sx = [
 [-1, 0, 1],
 [-2, 0, 2],
 [-1, 0, 1]
]
```

### result 
```
[
 [0,0,0,0,0,0,0,0],
 [0,1,1,0,0,-1,-1,0], 
 [0,3,3,0,0,-3,-3,0],
 [0,4,4,0,0,-4,-4,0], 
 [0,4,4,0,0,-4,-4,0],
 [0,3,3,0,0,-3,-3,0], 
 [0,1,1,0,0,-1,-1,0],
 [0,0,0,0,0,0,0,0]
]
```