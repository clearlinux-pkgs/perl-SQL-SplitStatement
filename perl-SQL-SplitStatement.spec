#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-SplitStatement
Version  : 1.00020
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/E/EM/EMAZEP/SQL-SplitStatement-1.00020.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EM/EMAZEP/SQL-SplitStatement-1.00020.tar.gz
Summary  : 'Split any SQL code into atomic statements'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-SQL-SplitStatement-bin = %{version}-%{release}
Requires: perl-SQL-SplitStatement-man = %{version}-%{release}
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

%description bin
bin components for the perl-SQL-SplitStatement package.


%package dev
Summary: dev components for the perl-SQL-SplitStatement package.
Group: Development
Requires: perl-SQL-SplitStatement-bin = %{version}-%{release}
Provides: perl-SQL-SplitStatement-devel = %{version}-%{release}
Requires: perl-SQL-SplitStatement = %{version}-%{release}
Requires: perl-SQL-SplitStatement = %{version}-%{release}

%description dev
dev components for the perl-SQL-SplitStatement package.


%package man
Summary: man components for the perl-SQL-SplitStatement package.
Group: Default

%description man
man components for the perl-SQL-SplitStatement package.


%prep
%setup -q -n SQL-SplitStatement-1.00020

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
/usr/lib/perl5/vendor_perl/5.28.2/SQL/SplitStatement.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/sql-split

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SQL::SplitStatement.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sql-split.1
