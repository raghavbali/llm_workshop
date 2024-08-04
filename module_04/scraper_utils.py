# Adapted From: https://gist.github.com/psychemedia/925e190e2afd15b050f32334ceff9ef6
import os
import nbformat

class NB_Markdown_Scraper:

    def __init__(self,input_paths=None):
        self.notebook_md_dict = dict()
        self.input_paths = input_paths

    def nbpathwalk(self,path):
        ''' Walk down a directory path looking for ipynb notebook files... '''
        valid_notebook_files = []
        for path, _, files in os.walk(path):
            if '.ipynb_checkpoints' in path or 'solutions' in path : continue
            for f in [i for i in files if i.endswith('.ipynb') and not i.startswith('dontcommit')]:
                valid_notebook_files.append(os.path.join(path, f))
        return valid_notebook_files


    def get_cell_contents(self,nb_fn, c_md=None, cell_typ=None):
        ''' Extract the content of Jupyter notebook cells. '''
        if cell_typ is None: cell_typ=['markdown']
        if c_md is None: c_md = []
        nb=nbformat.read(nb_fn,nbformat.NO_CONVERT)
        _c_md=[i for i in nb.cells if i['cell_type'] in cell_typ]
        ix=len(c_md)
        for c in _c_md:
            c.update( {"ix":str(ix)})
            c.update( {"title":nb_fn})
            ix = ix+1
        c_md = c_md + _c_md
        return c_md


    # scraper
    def scrape_markdowns(self):
        for directory in self.input_paths:
            directory_notebooks = self.nbpathwalk(directory)
            for notebook in directory_notebooks:
                notebook_cells = self.get_cell_contents(notebook, cell_typ=['markdown'])
                notebook_name = '_'.join(notebook.split('/')[1:]).split('.')[0]
                self.notebook_md_dict[notebook_name] = ' '.join([cell['source'] for cell in sorted(notebook_cells, 
                                                                                                   key=lambda d: d['ix'])])
            