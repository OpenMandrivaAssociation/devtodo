%define	name	devtodo
%define	version	0.1.19
%define	release	%mkrel 1

Name:		%{name}
Summary:	Todo displays and manages heirarchical lists of prioritized tasks
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
URL:		http://swapoff.org/DevTodo
Group:		Development/Other
Buildrequires:	readline-devel ncurses-devel glibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL

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

%build
%configure
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

