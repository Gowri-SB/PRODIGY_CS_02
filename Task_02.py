from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Perform encryption using XOR operation with the key
    encrypted_array = img_array ^ key
    
    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Perform decryption using XOR operation with the key
    decrypted_array = img_array ^ key
    
    # Convert back to image and save
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Image Encryption and Decryption")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Operation mode")
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer)")
    parser.add_argument("output", help="Path to save the output image")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.image, args.key, args.output)
    elif args.mode == "decrypt":
        decrypt_image(args.image, args.key, args.output)
