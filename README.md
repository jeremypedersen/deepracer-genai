**Last Updated: 2024-07-15**

# DeepRacer GenAI

A port of the Amazon AWS [DPR401 Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d8a88732-5154-49ac-9725-033c0bc74029/en-US/20-environment-setup#set-up-the-sagemaker-studio-notebook-workspace) into Chinese. 

Updates include:
- The instructions and explanations in each Jupyter notebook are now in Chinese
- Anthropic's *Claude Instant* model has been replaced with *Mistral Large*, as Anthropic [does not support users in Mainland China](https://www.anthropic.com/supported-countries)

**Note:** To help save a couple steps when setting up the environment, the Jupyter Notebooks, DeepRacer models, and other artifacts from the DPR401 lab have been downloaded from [this workshop link](https://static.us-east-1.prod.workshops.aws/public/459c0910-3a2e-4215-9b2c-2cdb2c5a4d14/assets/code_repo.tgz) and included directly into this repo.

## Other Notes

The lab has been altered so that:

1. Permissions to access S3 are no longer required (example models are stored and processed locally)
2. There is no dependency on DeepRacer, so the lab can be run in environments without access to `us-east-`
3. Lab 2 uses preexisting "enhanced" track images from Stable Diffusion, so there is no need to set up and run an SD model

Although these changes make the lab a little less "hands on", they allow the lab to be run in any region where SageMaker Notebooks are available. A single `t2.medium` or `t3.medium` notebook instance is now sufficient to run the lab