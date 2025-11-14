package com.example.demo.controllers;

import com.example.demo.models.UsuarioModel;
import com.example.demo.services.UsuarioService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/usuarios") 
public class UsuarioController {

    @Autowired
    UsuarioService usuarioService;

    @PostMapping()
    public UsuarioModel guardarUsuario(@RequestBody UsuarioModel usuario) {
        return this.usuarioService.guardarUsuario(usuario);
    }
    @GetMapping()
    public List<UsuarioModel> obtenerTodosLosUsuarios() {
        return usuarioService.obtenerTodosLosUsuarios();
    }

    @GetMapping("/{id}")
    public ResponseEntity<UsuarioModel> obtenerUsuarioPorId(@PathVariable("id") Long id) {
        Optional<UsuarioModel> usuario = usuarioService.obtenerUsuarioPorId(id);

        if (usuario.isPresent()) {
            return ResponseEntity.ok(usuario.get()); // Retorna 200 OK con el usuario
        } else {
            return ResponseEntity.notFound().build(); // Retorna 404 Not Found
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<UsuarioModel> actualizarUsuario(@PathVariable("id") Long id, @RequestBody UsuarioModel detallesUsuario) {
        UsuarioModel usuarioActualizado = usuarioService.actualizarUsuario(id, detallesUsuario);

        if (usuarioActualizado != null) {
            return ResponseEntity.ok(usuarioActualizado); // Retorna 200 OK con el usuario actualizado
        } else {
            return ResponseEntity.notFound().build(); // Retorna 404 Not Found
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarUsuario(@PathVariable("id") Long id) {
        boolean eliminado = usuarioService.eliminarUsuario(id);

        if (eliminado) {
            return ResponseEntity.noContent().build(); // Retorna 204 No Content (éxito)
        } else {
            return ResponseEntity.notFound().build(); // Retorna 404 Not Found (no se pudo borrar)
        }
    }
}