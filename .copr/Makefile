# .copr/Makefile for COPR make_srpm builds

NAME := sfizz-ui
VERSION := 1.2.3
SPECFILE := ../rpm/sfizz-plugins-only.spec

srpm:
	# Create source tarball from current commit
	git archive --format=tar.gz --prefix=$(NAME)-$(VERSION)/ HEAD > $(NAME)-$(VERSION).tar.gz

	# Build SRPM with rpmbuild
	rpmbuild -bs $(SPECFILE) \
		--define "_sourcedir $(PWD)" \
		--define "_srcrpmdir $(outdir)"
