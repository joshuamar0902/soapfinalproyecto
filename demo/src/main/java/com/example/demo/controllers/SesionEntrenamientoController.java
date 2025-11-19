package com.example.demo.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


import com.example.demo.models.SesionEntrenamientoModel;
import com.example.demo.services.SesionEntrenamientoService;

@RestController
@RequestMapping("/api/sesion_entrenamiento")
public class SesionEntrenamientoController {
    @Autowired
    private SesionEntrenamientoService sesionEntrenamientoService;

    @GetMapping
    public List<SesionEntrenamientoModel> getAllSesionesEntrenamiento() {
        return sesionEntrenamientoService.getAllSesionesEntrenamiento();
    }

    @GetMapping("/{id}")
    public ResponseEntity<SesionEntrenamientoModel> getSesionEntrenamientoById(@PathVariable Long id) {
        Optional <SesionEntrenamientoModel> sesionEntrenamiento = sesionEntrenamientoService.getSesionEntrenamientoById(id);
        return sesionEntrenamiento.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());        
    }

    @PostMapping
    public SesionEntrenamientoModel createSesionEntrenamiento(@RequestBody SesionEntrenamientoModel sesionEntrenamiento) {
        return sesionEntrenamientoService.saveSesionEntrenamiento(sesionEntrenamiento);
    }

    @PutMapping("/{id}")
    public ResponseEntity<SesionEntrenamientoModel> updateSesionEntrenamiento(@PathVariable Long id, @RequestBody SesionEntrenamientoModel sesionEntrenamientoDetails) {
        Optional<SesionEntrenamientoModel> sesionEntrenamientoOptional = sesionEntrenamientoService.getSesionEntrenamientoById(id);
        if (sesionEntrenamientoOptional.isPresent()) {
            SesionEntrenamientoModel sesionEntrenamientoToUpdate = sesionEntrenamientoOptional.get();
            sesionEntrenamientoToUpdate.setId_sesion(sesionEntrenamientoDetails.getId_sesion());
            sesionEntrenamientoToUpdate.setFechaHoraInicio(sesionEntrenamientoDetails.getFechaHoraInicio());
            sesionEntrenamientoToUpdate.setFechaHoraFin(sesionEntrenamientoDetails.getFechaHoraFin());
            sesionEntrenamientoToUpdate.setTipoActividad(sesionEntrenamientoDetails.getTipoActividad());
            sesionEntrenamientoToUpdate.setDuracionSegundos(sesionEntrenamientoDetails.getDuracionSegundos());
            sesionEntrenamientoToUpdate.setDistanciaMetros(sesionEntrenamientoDetails.getDistanciaMetros());
            sesionEntrenamientoToUpdate.setCaloriasQuemadas(sesionEntrenamientoDetails.getCaloriasQuemadas());
            sesionEntrenamientoToUpdate.setLatitudInicio(sesionEntrenamientoDetails.getLatitudInicio());
            sesionEntrenamientoToUpdate.setLongitudInicio(sesionEntrenamientoDetails.getLongitudInicio());
            sesionEntrenamientoToUpdate.setRitmoPromedio(sesionEntrenamientoDetails.getRitmoPromedio());
            sesionEntrenamientoToUpdate.setUsuario(sesionEntrenamientoDetails.getUsuario());
            SesionEntrenamientoModel updatedSesionEntrenamiento = sesionEntrenamientoService.saveSesionEntrenamiento(sesionEntrenamientoToUpdate);
            return ResponseEntity.ok(updatedSesionEntrenamiento);
        } else {
            return ResponseEntity.notFound().build();
        }

    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSesionEntrenamiento(@PathVariable Long id) {
        Optional<SesionEntrenamientoModel> sesionEntrenamiento = sesionEntrenamientoService.getSesionEntrenamientoById(id);
        if (sesionEntrenamiento.isPresent()) {
            sesionEntrenamientoService.deleteSesionEntrenamiento(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}