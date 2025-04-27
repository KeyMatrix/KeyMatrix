import React, { useRef } from 'react';
import { useFrame } from '@react-three/fiber';
import { useGLTF } from '@react-three/drei';

export function Avatar({ state }) {
  const group = useRef();
  const { scene } = useGLTF(`/avatars/${state}.glb`);

  useFrame(() => {
    if (group.current) {
      group.current.rotation.y += 0.003;
    }
  });

  return <primitive object={scene} ref={group} scale={1.5} />;
}
