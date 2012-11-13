%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	xcb-util's xcb-renderutil
Name:		xcb-util-renderutil
Version:	0.3.8
Release:	%mkrel 1
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%name-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	xcb-util-devel >= 0.3.8
BuildRequires:	x11-util-macros
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{libname}
Summary:	xcb-util-renderutil library package
Group:		System/X11

%description -n %{libname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This is the xcb-util-renderutil library package.

%package -n %{develname}
Summary:	xcb-util-renderutil development files
Group:		Development/C
Provides: 	libxcb-util-renderutil-devel = %{version}-%{release}
Provides:	xcb-util-renderutil-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.8
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.8

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_libdir}/libxcb-render-util.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/xcb/xcb_renderutil.h
%{_libdir}/libxcb-render-util.a
%{_libdir}/libxcb-render-util.la
%{_libdir}/libxcb-render-util.so
%{_libdir}/pkgconfig/xcb-renderutil.pc