%global provider	github
%global provider_tld	com
%global project		percona
%global repo		grafana-dashboards
%global provider_prefix	%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path	%{provider_prefix}
%global commit		99180110d8230541bf9e1b8dedf0b29c00ee4f59
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%define build_timestamp %(date -u +"%y%m%d%H%M")

Name:		%{project}-dashboards
Version:	1.1.0
Release:	1.%{build_timestamp}.%{shortcommit}%{?dist}
Summary:	Grafana dashboards for MySQL and MongoDB monitoring using Prometheus

License:	AGPLv3
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

BuildArch:	noarch
Requires:	percona-grafana python python-requests
Provides:	percona-grafana-dashboards = %{version}-%{release}

%description
Grafana dashboards for MySQL and MongoDB monitoring using Prometheus.
This is a set of Grafana dashboards for database and system monitoring
using Prometheus datasource.
Dashboards are also a part of Percona Monitoring and Management project.


%prep
%setup -q -n %{repo}-%{commit}


%build


%install
install -d %{buildroot}%{_datadir}/%{name}
cp -pav ./* %{buildroot}%{_datadir}/%{name}/
echo %{version} > %{buildroot}%{_datadir}/%{name}/VERSION


%files
%license LICENSE
%doc README.md LICENSE
%{_datadir}/%{name}


%changelog
* Thu Feb  2 2017 Mykola Marzhan <mykola.marzhan@percona.com> - 1.1.0-1
- add build_timestamp to Release value

* Thu Dec 15 2016 Mykola Marzhan <mykola.marzhan@percona.com> - 1.0.7-1
- init version
