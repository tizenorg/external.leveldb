Name:   	leveldb
Summary:    leveldb library
Version: 	1.1
Release:    1
Group:      libs
License:    Google
Source0:    %{name}-%{version}.tar.gz

%description
Description: leveldb


%package -n libleveldb
Summary:   leveldb library.
Group:     Development/Libraries
	
Provides: libleveldb.so 	
Provides: libmemenv.so

%description -n libleveldb
Description: leveldb library.

%prep
%setup -q

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files -n libleveldb
%defattr(-,root,root,-)
%{_libdir}/libleveldb.so
%{_libdir}/libleveldb.so.0
%{_libdir}/libleveldb.so.1.1.0
%{_libdir}/libmemenv.so
%{_libdir}/libmemenv.so.0
%{_libdir}/libmemenv.so.1.1.0
%{_libdir}/pkgconfig/leveldb.pc
%{_libdir}/pkgconfig/memenv.pc
%{_includedir}/leveldb/*.h
%{_includedir}/helpers/memenv/*.h
