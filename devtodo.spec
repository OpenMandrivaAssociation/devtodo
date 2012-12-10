%define	name	devtodo
%define	version	0.1.20
%define	release	%mkrel 4

Name:		%{name}
Summary:	Todo displays and manages heirarchical lists of prioritized tasks
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		devtodo-0.1.20-fix-gcc43.patch
URL:		http://swapoff.org/DevTodo
Group:		Development/Other
Buildrequires:	readline-devel ncurses-devel glibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2

%description
Todo is a program to display and manage a hierarchical, prioritized list of
outstanding work, or just reminders.

The program itself is assisted by a few shell scripts that override default
builtins. Specifically, cd, pushd and popd are overridden so that when using
one of these commands to enter a directory, the todo will display any
outstanding items in that directory.

For much more complete information please refer to the man page (devtodo(1)).

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc AUTHORS README COPYING INSTALL NEWS QuickStart doc/todorc.example doc/scripts.sh doc/scripts.tcsh ChangeLog
%config(noreplace) %{_sysconfdir}/todorc
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.20-4mdv2011.0
+ Revision: 617576
- the mass rebuild of 2010.0 packages

* Tue Jun 02 2009 Jérôme Brenier <incubusss@mandriva.org> 0.1.20-3mdv2010.0
+ Revision: 382107
- use configure2_5x
- fix build with gcc 4.3 (1 patch)
- fix license (GPLv2)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 22 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.20-1mdv2008.1
+ Revision: 101076
- Version 0.1.20

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 0.1.19-2mdv2008.0
+ Revision: 72306
- patch 0: fix build
- use %%mkrel


* Wed Jun 08 2005 Lenny Cartier <lenny@mandriva.com> 0.1.19-1mdk
- 0.1.19

* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.18-1mdk
- 0.1.18
- update url
- wipe out buildroot at the beginning of %%install, not %%prep
- cosmetics

* Wed Jun 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1.17-3mdk
- rebuild

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1.17-2mdk
- adjust buildrequires

* Thu Apr 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1.17-1mdk
- 0.1.17

* Fri Dec 20 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1.16-1mdk
- 0.1.16

* Wed Dec 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1.15-1mdk
- 0.1.15
- from Wesley J. Landaker <landaker@ieee.org> :
	- Created Mandrake RPM by adapting/fixing ASPLinux specfile.
	- Added missing files from doc directory to the specfile.
	- Made package relocateable.

* Thu Oct 18 2001 Alexandr D. Kanevskiy <kad@asplinux.ru>
- updated to 0.1.11

