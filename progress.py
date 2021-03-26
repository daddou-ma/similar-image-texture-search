import sys
import shutil

def map_with_progress(callback, array):
    (width, _) = list(shutil.get_terminal_size())
    length = len(array)
    barwidth = width - 10
    
    def callback_with_progress(index, item):
        filled = (index * barwidth) // length 
        empty = barwidth - filled
        
        sys.stdout.write('\r{fillbar}{emptybar} {index}/{length}'.format(
            fillbar=('█' * filled),
            emptybar=('-' * empty),
            index=str(index).zfill(4),
            length=str(length).zfill(4),
        ))
        sys.stdout.flush()

        return callback(item)

    return map(callback_with_progress, list(range(1, length + 1)), array)
