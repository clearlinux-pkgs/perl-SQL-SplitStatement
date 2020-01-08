#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-SplitStatement
Version  : 1.00020
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/E/EM/EMAZEP/SQL-SplitStatement-1.00020.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EM/EMAZEP/SQL-SplitStatement-1.00020.tar.gz
Summary  : 'Split any SQL code into atomic statements'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-SQL-SplitStatement-bin = %{version}-%{release}
Requires: perl-SQL-SplitStatement-license = %{version}-%{release}
Requires: perl-SQL-SplitStatement-man = %{version}-%{release}
Requires: perl-SQL-SplitStatement-perl = %{version}-%{release}
Requires: perl(SQL::Tokenizer)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Fast)
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Regexp::Common)
BuildRequires : perl(SQL::Tokenizer)
BuildRequires : perl(Test::Exception)

%description
NAME
SQL::SplitStatement - Split any SQL code into atomic statements
VERSION
version 1.00020

%package bin
Summary: bin components for the perl-SQL-SplitStatement package.
Group: Binaries
Requires: perl-SQL-SplitStatement-license = %{version}-%{release}

%description bin
bin components for the perl-SQL-SplitStatement package.


%package dev
Summary: dev components for the perl-SQL-SplitStatement package.
Group: Development
Requires: perl-SQL-SplitStatement-bin = %{version}-%{release}
Provides: perl-SQL-SplitStatement-devel = %{version}-%{release}
Requires: perl-SQL-SplitStatement = %{version}-%{release}

%description dev
dev components for the perl-SQL-SplitStatement package.


%package license
Summary: license components for the perl-SQL-SplitStatement package.
Group: Default

%description license
license components for the perl-SQL-SplitStatement package.


%package man
Summary: man components for the perl-SQL-SplitStatement package.
Group: Default

%description man
man components for the perl-SQL-SplitStatement package.


%package perl
Summary: perl components for the perl-SQL-SplitStatement package.
Group: Default
Requires: perl-SQL-SplitStatement = %{version}-%{release}

%description perl
perl components for the perl-SQL-SplitStatement package.


%prep
%setup -q -n SQL-SplitStatement-1.00020
cd %{_builddir}/SQL-SplitStatement-1.00020

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SQL-SplitStatement
cp %{_builddir}/SQL-SplitStatement-1.00020/LICENSE %{buildroot}/usr/share/package-licenses/perl-SQL-SplitStatement/d4427d2ab15fe70c339dcd95ed4861c30e06e5a0
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sql-split

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SQL::SplitStatement.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SQL-SplitStatement/d4427d2ab15fe70c339dcd95ed4861c30e06e5a0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sql-split.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/SQL/SplitStatement.pm
