package com.example.demo.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.models.FrecuenciaCardiacaModel;



@Repository
public interface IFrecuenciaCardiacaRepository extends JpaRepository<FrecuenciaCardiacaModel, Long> {

    
}