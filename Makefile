help: ## help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: local
local: ## 本地上传pypi
	command -v twine || pip install twine -i https://mirrors.51talk.com/pypi/simple  
	python setup.py sdist
	twine upload dist/*

.PHONY: image
image: ## 构建docker镜像
	docker build -t opencodo/python .
	docker push opencodo/python
