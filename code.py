import numpy as np
import matplotlib.pyplot as plt

def linear_mapping(image, a, b):
    return (image - a) / (b - a)

def non_linear_mapping(image):
    return np.log(1 + image)

def digital_negative(image):
    return 255 - image

def histogram_stretch(image, low, high):
    return np.clip((image - low) * 255.0 / (high - low), 0, 255).astype(np.uint8)

def histogram_shrink(image, low, high):
    return np.clip((image - low) * 255.0 / (high - low), 0, 255).astype(np.uint8)

def plot_histogram(image):
    plt.hist(image.flatten(), bins=256, range=(0,256), density=True, color='gray')
    plt.xlabel('Pixel Value')
    plt.ylabel('Normalized Frequency')
    plt.title('Histogram')
    plt.show()


def main():
    image = np.random.randint(0, 256, size=(100, 100)).astype(np.uint8)

    while True:
        print("\n1. Linear Mapping")
        print("2. Non-linear Mapping")
        print("3. Digital Negative")
        print("4. Histogram Stretch")
        print("5. Histogram Shrink")
        print("6. Plot Histogram")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Exiting...")
            break

        elif choice == 6:
            plot_histogram(image)

        else:
            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please enter a valid option.")
                continue

            low = int(input("Enter lower bound: "))
            high = int(input("Enter upper bound: "))

            if choice == 1:
                result = linear_mapping(image, low, high)
                title = 'Linear Mapping Result'
            elif choice == 2:
                result = non_linear_mapping(image)
                title = 'Non-linear Mapping Result'
            elif choice == 3:
                result = digital_negative(image)
                title = 'Digital Negative Result'
            elif choice == 4:
                result = histogram_stretch(image, low, high)
                title = 'Histogram Stretch Result'
            elif choice == 5:
                result = histogram_shrink(image, low, high)
                title = 'Histogram Shrink Result'

            plt.imshow(result, cmap='gray')
            plt.title(title)
            plt.show()

if __name__ == "__main__":
    
    main()
