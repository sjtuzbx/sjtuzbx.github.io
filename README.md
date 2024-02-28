## Pelican blog for my Github Pages

### Usage

1. Use `python -m pip install "pelican[markdown]"` to install [pelican](https://docs.getpelican.com/en/latest/quickstart.html)
2. Use `python -m pip install pelican-render-math` to install `render-math` plugin
3. Write your blog in markdown format and put it into `content/` folder
4. Use `make html` to build your site
5. Use `make serve` to see a live version in `localhost:8000`

### Customization

* See [pelican-themes](https://github.com/getpelican/pelican-themes) to choose what your love
* Add `THEME = 'pelican-themes/your-theme' ` in `pelicanconf.py` 