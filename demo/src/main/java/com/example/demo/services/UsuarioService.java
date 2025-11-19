package com.example.demo.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.example.demo.models.UsuarioModel;
import com.example.demo.repositories.IUsuarioRepository;

@Service
public class UsuarioService {
    
    @Autowired
    private IUsuarioRepository usuarioRepository;

    public List<UsuarioModel> getAllUsuarios() {
        return usuarioRepository.findAll();
    }

    public Optional<UsuarioModel>  getUsuarioById(Long id_usuario) {
        return usuarioRepository.findById(id_usuario);
    }

    public UsuarioModel saveUsuario(UsuarioModel usuario) {
        return usuarioRepository.save(usuario);
    }

    public void deleteUsuario(Long id_usuario) {
        usuarioRepository.deleteById(id_usuario);
    }

    
}