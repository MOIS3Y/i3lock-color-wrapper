{
  description = ''
    Pre-configured script to run i3lock-color
    with the ability to change the color scheme and some parameters'';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default-linux";
    flake-utils = {
      url = "github:numtide/flake-utils";
      inputs.systems.follows = "systems";
    };
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python3;
        pythonPackages = python.pkgs;
      in {
      packages = rec {
        i3lock-run = pythonPackages.buildPythonApplication {
          pname = "i3lock-run";
          version = "0.1.0";
          format = "pyproject";
          src = self;

          nativeBuildInputs = [
            pythonPackages.poetry-core
          ];
          dependencies = [
            pkgs.i3lock-color
          ];
        };
        default = i3lock-run;
      };
      apps = rec {
        i3lock-run = flake-utils.lib.mkApp {
          drv = self.packages.${system}.i3lock-run;
        };
        default = i3lock-run;
      };

      devShells.default = pkgs.mkShell {
        buildInputs = [
          python
          pkgs.poetry
        ];

        shellHook = ''
          poetry env use ${python}/bin/python
          poetry install
        '';
      };
  });
}
