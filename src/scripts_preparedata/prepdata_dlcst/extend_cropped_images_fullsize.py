
import argparse

from common.functionutil import makedir, list_files_dir, join_path_names, basename, basename_filenoext, fileextension,\
    get_pattern_prefix_filename, find_file_inlist_same_prefix, read_dictionary
from dataloaders.imagefilereader import ImageFileReader
from imageoperators.imageoperator import ExtendImage, FlipImage


def main(args):

    # SETTINGS
    def name_output_images_files(in_name: str):
        return basename_filenoext(in_name) + '.nii.gz'
    # --------

    list_input_images_files = list_files_dir(args.inputdir)
    list_input_reference_files = list_files_dir(args.reference_dir)
    dict_input_boundboxes = read_dictionary(args.boundboxes_file)
    pattern_search_input_files = get_pattern_prefix_filename(list_input_reference_files[0])

    makedir(args.outputdir)

    for i, in_image_file in enumerate(list_input_images_files):
        print("\nInput: \'%s\'..." % (basename(in_image_file)))

        in_crop_image = ImageFileReader.get_image(in_image_file)
        print("Original dims: \'%s\'..." % (str(in_crop_image.shape)))

        if fileextension(in_image_file) == '.nii.gz':
            inout_metadata = ImageFileReader.get_image_metadata_info(in_image_file)
        else:
            inout_metadata = None

        in_reference_file = find_file_inlist_same_prefix(basename(in_image_file), list_input_reference_files,
                                                         pattern_prefix=pattern_search_input_files)
        print("Reference file: \'%s\'..." % (basename(in_reference_file)))

        # 1 step: invert image
        in_crop_image = FlipImage.compute(in_crop_image, axis=0)
        # 2 step: extend image
        in_boundbox = dict_input_boundboxes[basename_filenoext(in_reference_file)]
        out_fullimage_shape = ImageFileReader.get_image_size(in_reference_file)
        out_full_image = ExtendImage.compute(in_crop_image, in_boundbox, out_fullimage_shape)

        out_image_file = join_path_names(args.outputdir, name_output_images_files(in_image_file))
        print("Output: \'%s\', of dims \'%s\'..." % (basename(out_image_file), str(out_full_image.shape)))

        ImageFileReader.write_image(out_image_file, out_full_image, metadata=inout_metadata)
    # endfor


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', type=str)
    parser.add_argument('outputdir', type=str)
    parser.add_argument('--reference_dir', type=str, default='RawImages/')
    parser.add_argument('--boundboxes_file', type=str, default='found_boundingBox_croppedCTinFull.npy')
    args = parser.parse_args()

    print("Print input arguments...")
    for key, value in vars(args).items():
        print("\'%s\' = %s" % (key, value))

    main(args)
