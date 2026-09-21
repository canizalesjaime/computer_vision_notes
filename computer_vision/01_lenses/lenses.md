# Lenses 

## Problems with pinhole
* Pin hole size(aperture) must be small
* The smaller size the less light that goes through
* If the pinhole is comparable to wavelength $\lambda$ of light diffraction effect blur the image
* Takes longer to generate  image 


**Lenses are used to avoid problem associated with pinholes, but same projection! gathers more light.**


## What they are
Lenses are optical elements that bend light rays so that rays coming from a single point in the 3D world converge to a single point on an image plane, such as a camera sensor or the human retina. Their main purpose is to form a sharp, bright image, something a simple pinhole camera cannot do efficiently.

In cameras and computer vision, lenses are often modeled using the thin lens approximation.


## Thin Lens Model
The thin lens equation relates object distance, image distance, and focal length:

1/f = 1/Z + 1/z

Where:
- `f` = focal length of the lens
- `Z` = distance from the lens to the object
- `z` = distance from the lens to the image plane (sensor)

This equation determines where the sensor must be placed for the image to be in focus.


## Focal Length

Focal length determines:
- Short focal length → wide field of view, strong perspective
- Long focal length → narrow field of view, zoomed-in appearance

In perspective projection models used in computer vision:

x = fX/Z  
y = fY/Z

The focal length `f` controls the magnification of the projected image.


## Aperture and Depth of Field

The aperture controls how much light enters the camera and affects depth of field (range of distances that appear sharp):

- Large aperture → shallow depth of field (background blurry)
- Small aperture → deep depth of field (more in focus)


## Lens Distortions

Real lenses are not perfect and can introduce:

- Radial distortion (barrel or pincushion)
- Tangential distortion (lens misalignment)

Camera calibration is performed to estimate lens parameters and correct distortions before applying geometric vision algorithms.


# A slightly deeper dive into lenses

## Aperture

The aperture is the opening in a lens through which light passes. It controls both how much light reaches the image sensor and how light rays spread as they pass through the lens.

### Key roles of the aperture

1. Light control  
- Larger aperture allows more light → brighter image  
- Smaller aperture allows less light → darker image  

2. Depth of field control  
- Larger aperture → shallow depth of field  
- Smaller aperture → deep depth of field  

### f-number (f-stop)

The aperture size is usually described by the f-number:

f/# = f / D

Where:
- f is the focal length
- D is the diameter of the aperture

A smaller f-number means a larger aperture opening.

### Intuition

The aperture determines how wide the cone of rays is for each image point. Wider cones lead to more blur when points are out of focus.


## Blur Circle (Circle of Confusion)

A blur circle is the image of a single 3D point when that point is not perfectly in focus.

### How blur circles form

- If a point lies exactly on the focus plane, rays converge to a point on the sensor.
- The focus plane is: The plane in 3D space where all points are imaged sharply (as points) on the sensor.
- If the point lies in front of or behind the focus plane, the rays intersect the sensor as a small disc instead of a point.
- This disc is called the blur circle.

### Factors affecting blur circle size

1. Distance from the focus plane  
   Greater distance → larger blur circle  

2. Aperture size  
   Larger aperture → larger blur circles  

3. Focal length  
   Longer focal length → larger blur circles for the same defocus  

### Visual interpretation

- Very small blur circle → appears sharp  
- Large blur circle → appears blurry  


## Depth of Field (DoF)

Depth of field is the range of object distances that appear acceptably sharp in an image.

### What defines “acceptable sharpness”

Sharpness is determined by whether the blur circle is smaller than a chosen threshold, called the acceptable circle of confusion.

### Factors affecting depth of field

- Aperture: smaller aperture → deeper DoF  
- Focal length: shorter focal length → deeper DoF  
- Focus distance: focusing farther away increases DoF  

### Approximate relationship

For a thin lens and distant scenes:

DoF ≈ (2 * u^2 * N * c) / f^2

Where:
- u is the focus distance
- N is the f-number
- c is the acceptable circle of confusion
- f is the focal length

### Interpretation

- Shallow depth of field isolates subjects
- Deep depth of field keeps more of the scene sharp


## Hyperfocal Distance

The hyperfocal distance is a special focus distance that maximizes depth of field.

### Definition

When a lens is focused at the hyperfocal distance:
- Everything from half that distance to infinity appears acceptably sharp.

### Formula

H = (f^2) / (N * c) + f

Where:
- f is the focal length
- N is the f-number
- c is the acceptable circle of confusion

### Practical use

- Common in landscape photography
- Allows large portions of the scene to be in focus without refocusing


## Relationship Between Concepts

Aperture controls the angular spread of rays through the lens.  
This spread determines the size of blur circles for out-of-focus points.  
Blur circle size determines whether points are considered sharp.  
The range of distances producing small enough blur circles defines the depth of field.  
The hyperfocal distance is the focus setting that maximizes this range toward infinity.


## Two-Lens Systems

Most cameras use multiple lenses. A two-lens system (compound lens) works as follows:

1. The first lens forms an intermediate image of the object.
2. The second lens treats that intermediate image as its object and forms the final image on the sensor.

Each lens obeys the thin lens equation independently. The total magnification of the system is the product of the magnifications of each lens:

M_total = M1 * M2,  where Mi = -zi / Zi

---

## Real-World Examples

- **Cameras**: multiple lenses focus light accurately and reduce optical aberrations.
- **Microscopes**: objective lens forms a magnified real image; eyepiece lens further magnifies it.
- **Telescopes**: objective lens collects light from distant objects; eyepiece lens magnifies angular size.

---

## Relation to Computer Vision

Even with multiple lenses, computer vision often simplifies the system to:

- A single effective focal length
- A single optical center

This works because vision geometry depends on the paths of light rays, not the internal lens structure.

