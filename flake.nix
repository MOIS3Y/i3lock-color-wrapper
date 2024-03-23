{
  description = ''
    Pre-configured script to run i3lock-color
    with the ability to change the color scheme and some parameters'';

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, poetry2nix, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication;
      inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryEnv;
    in {

    # Executed by `nix build .#<name>
    # ? Example: nix build .#i3lock-color-wrapper 
    packages.${system} = {
      i3lock-color-wrapper = with pkgs; mkPoetryApplication { 
        projectDir = self; 
        preferWheels = true;
        propagatedBuildInputs = [
          i3lock-color
        ];
      };
      default = self.packages.${system}.i3lock-color-wrapper;
    };
    
    # Executed by `nix run . -- <args?>`
    # ? example: nix run .#i3lock-color-wrapper -- --version
    apps.${system}.i3lock-color-wrapper = {
      type = "app";
      program = "${self.packages.${system}.i3lock-color-wrapper}/bin/i3lock-run";
    };

    # Used by `nix develop`
    # ? Example: nix develop .#i3lock-color-wrapper
    devShells.${system}.i3lock-color-wrapper = pkgs.mkShellNoCC {
      shellHook = ''
        echo
        echo "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀"
        echo "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄"
        echo "-- -- -- -- -- -- -- -- -- -- -"
        echo
      '';
      packages = with pkgs; [
        (mkPoetryEnv { projectDir = self; preferWheels = true; })
        i3lock-color
      ];
    };
  };
}
