# fin_gamma


```shell
cd runner
docker build -t ctadp .
docker run --rm -v $(pwd):/pipeline -w /pipeline ctadp /bin/bash run.sh
```

# References
- [ctools package](http://cta.irap.omp.eu/ctools/)
- [conda_docker_tips](https://jcristharif.com/conda-docker-tips.html)
- [conda_docker](https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html)
- [publish_docker_images](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images)
- [conda_image](https://pythonspeed.com/articles/activate-conda-dockerfile/)
- [ctools_setup](http://cta.irap.omp.eu/ctools/admin/install_conda.html)
- [running python in container](https://www.timsanteford.com/posts/running-a-python-script-in-docker/)


