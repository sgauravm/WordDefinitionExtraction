from pathlib import Path
import pandas as pd
import os
import numpy as np

def get_data_slt(dir_path):
    file_names = os.listdir(dir_path)
    sentences = []
    labels =[]
    tags = []
    for fn in file_names:
        if fn.endswith(".deft"):
            file_path = os.path.join(dir_path,fn)
            fp = Path(file_path)
            text = fp.read_text().strip()
            lines = text.split('\n\n')
            for line in lines:
                words = line.split('\n')
                sent = []
                tag = []
                is_def = 0
                for word in words:
                    elems = word.split('\t')
                    if len(elems)== 8:
                        if len(elems[4].split('-'))>1 and   elems[4].split('-')[1]=='Ordered':
                            sent = []
                            tag = []
                            break
                        sent.append(elems[0])
                        tag.append(elems[4])
                        if elems[4].split('-')[-1]=='Definition':
                            is_def = 1

                if len(sent)!=0:
                    sentences.append(sent)
                    tags.append(tag)
                    labels.append(is_def)
    return sentences,labels,tags