FROM condaforge/miniforge3:latest
COPY environment.yml /tmp/environment.yml
RUN mamba env create -f /tmp/environment.yml && mamba clean -afy
ENV PATH=/opt/conda/envs/bio/bin:$PATH
