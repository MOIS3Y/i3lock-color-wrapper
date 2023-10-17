{
  description = ''
    Pre-configured script to run i3lock-color
    with the ability to change the color scheme and some parameters'';

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
    packages.${system}.i3lock-color-wrapper = with pkgs;
      poetry2nix.mkPoetryApplication {
        projectDir = self;
        preferWheels = true;
        propagatedBuildInputs = [
          i3lock-color
        ];
      };
    devShells.${system}.i3lock-color-wrapper = pkgs.mkShellNoCC {
      shellHook = ''
        echo
        echo "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀"
        echo "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄"
        echo "-- -- -- -- -- -- -- -- -- -- -"
        echo
      '';
      packages = with pkgs; [
        (poetry2nix.mkPoetryEnv { projectDir = self; preferWheels = true; })
        i3lock-color
      ];
    };
  };
}
