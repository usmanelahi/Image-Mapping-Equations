**Title: Mapping Equations and Image Operations**

**Introduction:**
This Python script offers functionality for various image mapping equations and operations. Users can select between linear and non-linear mapping, perform digital negative, histogram stretch, and histogram shrink operations. The script allows users to specify input ranges for certain operations and provides visualizations of the results.

**Usage:**

1. **Running the Script:**

   - Execute the script using Python interpreter:
     ```
     python3 code.py
     ```

2. **Functionality:**
   - Upon execution, the user is presented with a menu to choose the desired operation.
   - Options include:
     - Linear Mapping
     - Non-linear Mapping
     - Digital Negative
     - Histogram Stretch
     - Histogram Shrink
     - Plot Histogram
     - Exit
   - Depending on the selected operation, the user may need to provide additional input such as range parameters.
   - Results are displayed using matplotlib.

**Components:**

1. **Linear Mapping:**

   - Maps pixel values linearly based on user-defined range (a, b).
   - Formula: \( \frac{{\text{{image}} - a}}{{b - a}} \)

2. **Non-linear Mapping:**

   - Applies a non-linear transformation to the image using the formula: \( \log(1 + \text{{image}}) \).

3. **Digital Negative:**

   - Inverts the pixel values, resulting in a negative image.

4. **Histogram Stretch:**

   - Stretches the histogram of the image based on user-defined range (low, high).
   - Formula: \( \text{{clip}}\left(\frac{{\text{{image}} - \text{{low}}}}{{\text{{high}} - \text{{low}}}} \times 255.0, 0, 255\right) \)

5. **Histogram Shrink:**

   - Shrinks the histogram of the image based on user-defined range (low, high).
   - Formula: \( \text{{clip}}\left(\frac{{\text{{image}} - \text{{low}}}}{{\text{{high}} - \text{{low}}}} \times 255.0, 0, 255\right) \)

6. **Plot Histogram:**
   - Displays the histogram of the original image using matplotlib.

**Conclusion:**
This Python script provides a user-friendly interface to perform various image mapping equations and operations. It offers flexibility in choosing input ranges and visualizing the results, making it suitable for educational and practical purposes in image processing.
