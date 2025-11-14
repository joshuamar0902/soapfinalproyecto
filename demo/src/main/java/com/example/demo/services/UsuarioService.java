package com.example.demo.services;

import com.example.demo.models.UsuarioModel;
import com.example.demo.repositories.IUsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UsuarioService {

    // Inyecta una instancia del repositorio
    @Autowired
    IUsuarioRepository usuarioRepository;

    public UsuarioModel guardarUsuario(UsuarioModel usuario) {
        return usuarioRepository.save(usuario);
    }

    public List<UsuarioModel> obtenerTodosLosUsuarios() {
        return usuarioRepository.findAll();
    }

    public Optional<UsuarioModel> obtenerUsuarioPorId(Long id) {
        return usuarioRepository.findById(id);
    }

    public UsuarioModel actualizarUsuario(Long id, UsuarioModel detallesUsuario) {
        Optional<UsuarioModel> usuarioOpt = usuarioRepository.findById(id);

        if (usuarioOpt.isEmpty()) {
            return null;
        }
        UsuarioModel usuarioExistente = usuarioOpt.get();
        usuarioExistente.setNombre(detallesUsuario.getNombre());
        usuarioExistente.setApellido(detallesUsuario.getApellido());
        usuarioExistente.setCorreoElectronico(detallesUsuario.getCorreoElectronico());
        usuarioExistente.setFechaDeNacimiento(detallesUsuario.getFechaDeNacimiento());
        usuarioExistente.setGenero(detallesUsuario.getGenero());
        usuarioExistente.setPeso(detallesUsuario.getPeso());
        usuarioExistente.setAltura(detallesUsuario.getAltura());

        return usuarioRepository.save(usuarioExistente);
    }
    public boolean eliminarUsuario(Long id) {
        try {
            usuarioRepository.deleteById(id);
            return true;
        } catch (EmptyResultDataAccessException e) {
            return false;
        } catch (Exception e) {
            return false;
        }
    }
}