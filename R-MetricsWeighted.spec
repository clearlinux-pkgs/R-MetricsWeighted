#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v13
# autospec commit: 2659038
#
Name     : R-MetricsWeighted
Version  : 1.0.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/MetricsWeighted_1.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MetricsWeighted_1.0.3.tar.gz
Summary  : Weighted Metrics and Performance Measures for Machine Learning
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
measures used in machine learning, including average unit deviances of
    the Bernoulli, Tweedie, Poisson, and Gamma distributions, see

%prep
%setup -q -n MetricsWeighted

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720114781

%install
export SOURCE_DATE_EPOCH=1720114781
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MetricsWeighted/DESCRIPTION
/usr/lib64/R/library/MetricsWeighted/INDEX
/usr/lib64/R/library/MetricsWeighted/Meta/Rd.rds
/usr/lib64/R/library/MetricsWeighted/Meta/features.rds
/usr/lib64/R/library/MetricsWeighted/Meta/hsearch.rds
/usr/lib64/R/library/MetricsWeighted/Meta/links.rds
/usr/lib64/R/library/MetricsWeighted/Meta/nsInfo.rds
/usr/lib64/R/library/MetricsWeighted/Meta/package.rds
/usr/lib64/R/library/MetricsWeighted/Meta/vignette.rds
/usr/lib64/R/library/MetricsWeighted/NAMESPACE
/usr/lib64/R/library/MetricsWeighted/NEWS.md
/usr/lib64/R/library/MetricsWeighted/R/MetricsWeighted
/usr/lib64/R/library/MetricsWeighted/R/MetricsWeighted.rdb
/usr/lib64/R/library/MetricsWeighted/R/MetricsWeighted.rdx
/usr/lib64/R/library/MetricsWeighted/doc/MetricsWeighted.R
/usr/lib64/R/library/MetricsWeighted/doc/MetricsWeighted.Rmd
/usr/lib64/R/library/MetricsWeighted/doc/MetricsWeighted.html
/usr/lib64/R/library/MetricsWeighted/doc/index.html
/usr/lib64/R/library/MetricsWeighted/help/AnIndex
/usr/lib64/R/library/MetricsWeighted/help/MetricsWeighted.rdb
/usr/lib64/R/library/MetricsWeighted/help/MetricsWeighted.rdx
/usr/lib64/R/library/MetricsWeighted/help/aliases.rds
/usr/lib64/R/library/MetricsWeighted/help/figures/logo.png
/usr/lib64/R/library/MetricsWeighted/help/paths.rds
/usr/lib64/R/library/MetricsWeighted/html/00Index.html
/usr/lib64/R/library/MetricsWeighted/html/R.css
/usr/lib64/R/library/MetricsWeighted/tests/testthat.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-accuracy-error.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-deviance.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-elescore.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-interface.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-performance-multimetric.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-plots.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-precision-recall-f1.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-probabilities.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-prop-within.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-regression.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-rsquared.R
/usr/lib64/R/library/MetricsWeighted/tests/testthat/test-stats.R
