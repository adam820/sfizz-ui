# .copr/Makefile for COPR make_srpm builds

NAME := sfizz-ui
VERSION := 1.2.3
SPECFILE := ../rpm/sfizz-plugins-only.spec

srpm:
	# Create source tarball from current commit
	mkdir -p tmp-src
	tar czf tmp-src/$(NAME)-$(VERSION).tar.gz \
		--transform "s,^,$(NAME)-$(VERSION)/," --exclude=.copr --exclude=tmp-src --exclude=.git --exclude=*.rpm --exclude=*.tar.gz ..
	mv tmp-src/$(NAME)-$(VERSION).tar.gz .
	rm -rf tmp-src

	# list the tar contents and show size
	tar tvf $(NAME)-$(VERSION).tar.gz
	ls -lh $(NAME)-$(VERSION).tar.gz

	# Build SRPM with rpmbuild
	rpmbuild -bs $(SPECFILE) \
		--define "_sourcedir $(PWD)" \
		--define "_srcrpmdir $(outdir)"
