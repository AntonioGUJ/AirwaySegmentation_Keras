
from common.functionutil import *
from dataloaders.imagefilereader import ImageFileReader
from imageoperators.imageoperator import CropImage, FlipImage
import argparse



def main(args):

    list_input_crop_images_files = list_files_dir(args.crop_images_dir)
    list_input_full_images_files = list_files_dir(args.full_images_dir)
    dict_input_bounding_boxes    = read_dictionary(args.found_boundingbox_file)


    names_files_different = []

    for i, (in_cropimage_file, in_fullimage_file) in enumerate(zip(list_input_crop_images_files, list_input_full_images_files)):
        print("\nInput: \'%s\'..." % (basename(in_cropimage_file)))
        print("Input 2: \'%s\'..." % (basename(in_fullimage_file)))

        in_crop_image = ImageFileReader.get_image(in_cropimage_file)
        in_full_image = ImageFileReader.get_image(in_fullimage_file)

        # 1 step: crop image
        in_bounding_box = dict_input_bounding_boxes[basename_filenoext(in_cropimage_file)]
        new_crop_image  = CropImage.compute(in_full_image, in_bounding_box)
        # 2 step: invert image
        new_crop_image  = FlipImage.compute(new_crop_image, axis=0)

        if (in_crop_image.shape == new_crop_image.shape):
            res_voxels_equal = np.array_equal(in_crop_image, new_crop_image)

            if res_voxels_equal:
                print("GOOD: Images are equal voxelwise...")
            else:
                names_files_different.append(basename(in_cropimage_file))
                message = "ERROR: Images are different..."
                catch_warning_exception(message)
        else:
            names_files_different.append(basename(in_cropimage_file))
            message = "ERROR: Images are different..."
            catch_warning_exception(message)
    # endfor

    if (len(names_files_different) == 0):
        print("\nGOOD: ALL IMAGE FILES ARE EQUAL...")
    else:
        print("\nERROR: Found \'%s\' files that are different. Names of files: \'%s\'..." %(len(names_files_different),
                                                                                            names_files_different))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('crop_images_dir', type=str)
    parser.add_argument('full_images_dir', type=str)
    parser.add_argument('--found_boundingbox_file', type=str, default='found_boundingBox_croppedCTinFull.npy')
    args = parser.parse_args()

    print("Print input arguments...")
    for key, value in vars(args).items():
        print("\'%s\' = %s" %(key, value))

    main(args)