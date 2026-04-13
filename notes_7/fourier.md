# Fourier Transforms


## Euler's Identity

Euler's Identity is:

$e^{jθ} = cosθ + j*sinθ$

Special case (Euler's identity proper):

$e^{jπ} + 1 = 0$

- Links the 5 fundamental numbers: 0, 1, π, e, j
- Shows the connection between exponentials, trig, and complex numbers

Using Euler's formula, any sinusoid can be written as:

$sinθ = \frac{e^{jθ} - e^{-jθ}}{2j}$ <br>
$cosθ = \frac{e^{jθ} + e^{-jθ}}{2}$

---

## Conversion 
Convert:
$f(t) = sin(2π*5t) + 0.5*sin(2π*20t)$

Using Euler's formula:

1. First term: $sin(2π*5t)$

$sin(2π*5t) = \frac{e^{j*2π*5t} - e^{-j*2π*5t}}{2j}$

2. Second term: $0.5*sin(2π*20t)$

$0.5*sin(2π*20t) = 0.5 * \frac{e^{j*2π*20t} - e^{-j*2π*20t}}{2j} = \frac{e^{j*2π*20t} - e^{-j*2π*20t}}{4j}$

Combined:

$f(t) = \frac{e^{j*2π*5t} - e^{-j*2π*5t}}{2j} + \frac{e^{j*2π*20t} - e^{-j*2π*20t}}{4j}$

- Now f(t) is expressed as a sum of complex exponentials  
- This is the form used in Fourier analysis

---

## Understanding waves

Given: $f(x) = A*sin(ω*x + φ) + c$

Term meanings:

* A    : Amplitude – peak height of the wave
* ω    : Angular frequency – how fast the wave oscillates, ω = 2π*f
* x    : Input variable (usually time t)
* φ    : Phase shift – horizontal shift of the wave
* c    : Vertical offset – moves the wave up/down

Example:

$f(x) = 3*sin(2π*10*x + π/4) + 2$

- Amplitude = 3 → wave peaks ±3 from baseline  
- Angular frequency = 2π*10 → frequency = 10 Hz  
- Phase shift = π/4 → wave shifted right by π/4 radians  
- Vertical offset = 2 → baseline at 2 instead of 0

---

## Fourier Transforms
A **Fourier transform** is a way to break down a signal (like a sound wave, image, or time-series data) into a combination of simple waves (sines and cosines). Think of it as answering this question: *“What frequencies make up this signal?”*<br><br>

Any complex signal can be represented as a sum of simple oscillations:

- Low frequency → slow changes  
- High frequency → rapid changes  

For example:
- A musical chord = multiple pure tones added together  
- The Fourier transform tells you *which tones* are present and *how strong* they are  

---

## Time domain vs Frequency domain
- **Time domain**: how a signal changes over time (what you usually see)
- **Frequency domain**: what frequencies exist in the signal

The Fourier transform converts:

time domain → frequency domain

---

## The formula
Here’s the continuous Fourier transform:
$X(f) = \int_{-\infty}^{\infty} x(t) \, e^{-j 2 \pi f t} \, dt$
- $ x(t) $: original signal (time domain)  
- $ X(f) $: frequency representation  
- $ e^{-i 2 \pi f t} $: complex sinusoid (basis function)

---

## What it’s really doing
You can think of it like this:

1. Take a sine wave of a certain frequency  
2. Compare it with your signal  
3. Measure how much of that frequency is present  
4. Repeat for all frequencies  

---

## Discrete version (what computers use)
In practice, we use the **Discrete Fourier Transform (DFT)** or the faster version:

- **FFT (Fast Fourier Transform)** → efficient algorithm

Used everywhere in:
- Audio processing (MP3s, speech recognition)
- Image compression (JPEG)
- Signal filtering
- Robotics & sensors
- **Computer vision** (image filtering)

---

## Example
Imagine a signal:

$f(t) = sin(2π·5t) + 0.5·sin(2π·20t)$

Fourier transform result:
- Peak at 5 Hz (strong)
- Peak at 20 Hz (weaker)

---

## Inverse transform
You can also go back:
$x(t) = \int_{-\infty}^{\infty} X(f) \, e^{j 2 \pi f t} \, df$

- Frequency → time domain  
- This is called the **inverse Fourier transform**

---

## Simple analogy
Think of a smoothie:
- Time domain = the smoothie  
- Frequency domain = the ingredients (banana, strawberry, etc.)  

Fourier transform = figuring out the recipe 

---


## Fast Fourier Transform (FFT)

The **Fast Fourier Transform (FFT)** is an efficient algorithm for computing the **Discrete Fourier Transform (DFT)**.

In simple terms:  
It does the *same thing* as the DFT—but **much faster**.

---

## What problem it solves
The DFT takes a signal with N samples and computes its frequency components.

Naively:
- DFT complexity = O(N^2) → slow for large data

FFT improves this to:
- O(N log N) → dramatically faster

---

## The DFT formula (what FFT computes)
$ X_k = \sum_{n=0}^{N-1} x_n \, e^{-i \frac{2\pi}{N} k n} $

- $x_n$: input signal  
- $X_k$: frequency components  
- N: number of samples  

---

## Key idea behind FFT
- DFT: tells you frequencies  
- FFT: computes it efficiently  

FFT uses a **divide-and-conquer** strategy:

1. Split the signal into:
   - even-indexed samples  
   - odd-indexed samples  

2. Recursively compute smaller DFTs  

3. Combine results using symmetry:
   - reuse computations instead of repeating them(eliminates redundant work)  

---


## Example (conceptual)
If you have 8 samples:

- DFT: computes everything directly  
- FFT:
  - splits into two groups of 4  
  - then 2  
  - then 1  
  - combines results efficiently  

---

## Where FFT is used

### Robotics / Embedded
- Filtering noisy sensor signals (ultrasonic, IMU)
- Detecting periodic vibrations in motors

### Audio
- Equalizers
- Pitch detection
- Compression (MP3)

### Images
- Blur/sharpen filters
- JPEG compression

### Signals
- Spectrum analyzers
- Communication systems
