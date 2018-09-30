
VERSION ?= '2.6.5'
PY_VERSION ?= 2
NAME ?= portable-ansible-py$(PY_VERSION)
TARGET ?= $(shell pwd)/target/ansible

.PHONY: package
package: prepare-in-docker-py
	rm *.rpm *.deb || echo
	docker run --rm -it -v $(CURDIR):$(CURDIR) -w $(CURDIR) alanfranz/fpm-within-docker:centos-7 fpm  -s dir -t rpm -n $(NAME) -v $(VERSION) -x "*.DS_Store" ./bin/=/usr/bin/ ./target/=/usr/local/ansible/

	docker run --rm -it -v $(CURDIR):$(CURDIR) -w $(CURDIR) alanfranz/fpm-within-docker:ubuntu-xenial fpm  -s dir -t deb -n $(NAME) -v $(VERSION) -x "*.DS_Store" ./bin/=/usr/bin/ ./target/=/usr/local/ansible/

.PHONY: clean
clean:
	@ echo "[INFO] Cleaning directory:" $(shell pwd)/target
	@ rm -rf \
		$(shell pwd)/target
	@ mkdir -p $(TARGET)/


.PHONY: post-clean
post-clean: deps
	echo '[INFO] Removing extra dirs and files' && \
		rm -rf \
			$(TARGET)/*.dist-info \
			$(TARGET)/*.egg-info \
			$(TARGET)/*.gz \
			$(TARGET)/*.whl \
			$(TARGET)/bin && \
	echo '[INFO] Removing __pycache__ dirs' && \
		find $(TARGET)/ -path '*/__pycache__/*' -delete
		find $(TARGET)/ -type d -name '__pycache__' -empty -delete

.PHONY: deps
deps:
	@ cp $(shell pwd)/__main__.py $(TARGET)/

.PHONY: prepare-py
prepare-py: clean
	@ echo '[INFO] Installing Ansible packages' && \
		pip install \
			ansible==$(VERSION) . \
			--target $(TARGET)/
	@ ln -s ansible target/ansible-playbook

.PHONY: prepare-in-docker-py
prepare-in-docker-py:
	@ echo '[INFO] Run docker container for building Ansible packages' && \
		docker run -ti --rm --name ansible-build \
			-v $(shell pwd):/data \
			python:$(PY_VERSION) /bin/sh -c "\
					cd /data && make prepare-py && make post-clean"

.PHONY: tarball-py
tarball-py: prepare-in-docker-py
	@ echo '[INFO] Building tarball' && \
		mkdir -p $(shell pwd)/builds && \
		tar cjf builds/$(NAME)-$(VERSION).tar.bz2 -C $(shell pwd)/target/ ansible