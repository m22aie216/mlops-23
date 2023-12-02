az login --scope https://management.core.windows.net//.default
az acr build --file ./docker/DependencyDockerfile --registry sreejesh23 --image base .
az acr build --file ./docker/FinalDockerfile --registry sreejesh23 --image exp .
