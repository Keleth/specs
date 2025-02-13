%define        _unpackaged_files_terminate_build 1
%define        gemname racc

Name:          gem-racc
Epoch:         1
Version:       1.7.3
Release:       alt2
Summary:       Ruby LALR(1) parser generator
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           http://i.loveruby.net/en/projects/racc/
Vcs:           https://github.com/tenderlove/racc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       %gemname.alternatives.erb
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0.1
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(test-unit-ruby-core) >= 1.0.5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(test-unit-ruby-core) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency test-unit-ruby-core >= 1.0.5,test-unit-ruby-core < 2
Requires:      racc = %EVR
Obsoletes:     ruby-racc < %EVR
Provides:      ruby-racc = %EVR
Provides:      gem(racc) = 1.7.3

%ruby_on_build_rake_tasks compile

%description
Racc is an LALR(1) parser generator. It is written in ruby itself, and generates
ruby programs.

NOTE: Ruby 1.8.x comes with Racc runtime module. You can run your parsers
generated by racc 1.4.x out of the box.


%package       -n racc
Version:       1.7.3
Release:       alt2
Summary:       Ruby LALR(1) parser generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета racc
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(racc) = 1.7.3
Requires(pre): alternatives >= 0:0.2.0-alt0.12

%description   -n racc
Ruby LALR(1) parser generator executable(s).

Racc is an LALR(1) parser generator. It is written in ruby itself, and generates
ruby programs.

NOTE: Ruby 1.8.x comes with Racc runtime module. You can run your parsers
generated by racc 1.4.x out of the box.

%description   -n racc -l ru_RU.UTF-8
Исполнямка для самоцвета racc.


%package       -n gem-racc-doc
Version:       1.7.3
Release:       alt2
Summary:       Ruby LALR(1) parser generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета racc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(racc) = 1.7.3

%description   -n gem-racc-doc
Ruby LALR(1) parser generator documentation files.

Racc is an LALR(1) parser generator. It is written in ruby itself, and generates
ruby programs.

NOTE: Ruby 1.8.x comes with Racc runtime module. You can run your parsers
generated by racc 1.4.x out of the box.

%description   -n gem-racc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета racc.


%package       -n gem-racc-devel
Version:       1.7.3
Release:       alt2
Summary:       Ruby LALR(1) parser generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета racc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(racc) = 1.7.3
Requires:      gem(rake) >= 13.0.1
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(test-unit-ruby-core) >= 1.0.5
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(test-unit-ruby-core) >= 2

%description   -n gem-racc-devel
Ruby LALR(1) parser generator development package.

Racc is an LALR(1) parser generator. It is written in ruby itself, and generates
ruby programs.

NOTE: Ruby 1.8.x comes with Racc runtime module. You can run your parsers
generated by racc 1.4.x out of the box.

%description   -n gem-racc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета racc.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
mkdir -p %buildroot%_altdir/
ruby -rerb -e 'File.open("%buildroot%_altdir/%gemname", "w") { |f| f.puts ERB.new(IO.read("%SOURCE1")).result }'
rm %buildroot%_bindir/%gemname

%check
%ruby_test

%files
%doc README.ja.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n racc
%doc README.ja.rdoc README.rdoc
%_altdir/%gemname

%files         -n gem-racc-doc
%doc README.ja.rdoc README.rdoc
%ruby_gemdocdir

%files         -n gem-racc-devel
%doc README.ja.rdoc README.rdoc


%changelog
* Wed May 15 2024 Pavel Skrylev <majioa@altlinux.org> 1:1.7.3-alt2
- * symlink to internal ruby binaries use alternatives engine;

* Tue Nov 28 2023 Pavel Skrylev <majioa@altlinux.org> 1:1.7.3-alt1
- ^ 1.6.1 -> 1.7.3

* Tue Dec 20 2022 Pavel Skrylev <majioa@altlinux.org> 1:1.6.1-alt1
- ^ 1.6.0.1 -> 1.6.1

* Fri Apr 01 2022 Pavel Skrylev <majioa@altlinux.org> 1:1.6.0.1-alt1
- ^ 1.5.1 -> 1.6.0[1]

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.5.1-alt1
- ^ 1.5.0 -> 1.5.1
- ! restored lost files by adding the compile pre stage

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1:1.5.0-alt1
- ^ 1.4.15 -> 1.5.0
- ! spec tags and syntax

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.4.15-alt2
- ! shebang line autoreplacement for excutables

* Wed Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.4.15-alt1
- > Ruby Policy 2.0
- 1.4.14 -> 1.4.15

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.4.14-alt3.1
- Rebuild with new Ruby autorequirements.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.14-alt3
- Build with rpm-build-ruby-0.2.2-alt2 for more deps.

* Thu Oct 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.14-alt2
- do not package ruby-racc-runtime.
  NOTE: Ruby 1.8.x comes with Racc runtime module.
  You can run your parsers generated by racc 1.4.x out of the box.

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.4.14-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1:1.4.6-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1:1.4.6-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 1:1.4.6-alt2
- Rebuild with new ruby.

* Mon Jul 06 2009 Alexey I. Froloff <raorn@altlinux.org> 1:1.4.6-alt1.1
- Built for Sisyphus
