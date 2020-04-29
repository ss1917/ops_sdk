help: ## help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: local
local: ## 本地上传pypi
	command -v twine || pip install twine -i https://pypi.tuna.tsinghua.edu.cn/simple
	python setup.py sdist
	twine upload dist/*
