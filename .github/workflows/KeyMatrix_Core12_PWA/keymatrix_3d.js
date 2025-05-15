
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0d0d0d);
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 5, 15);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(10, 10, 10);
scene.add(light, new THREE.AmbientLight(0x404040));

const nodes = [
  { name: 'PRIME CORE', position: [0, 0, 0] },
  { name: 'MINDGATE', position: [5, 0, 0] },
  { name: 'SINGULARITY', position: [-5, 0, 0] },
  { name: 'CORE', position: [0, 5, 0] },
  { name: 'TRANSFORMATION', position: [0, -5, 0] },
];
const nodeGroup = new THREE.Group();
scene.add(nodeGroup);

nodes.forEach(node => {
  const sphere = new THREE.Mesh(
    new THREE.SphereGeometry(0.5, 32, 32),
    new THREE.MeshStandardMaterial({ color: new THREE.Color(0x00bfff) })
  );
  sphere.position.set(...node.position);
  nodeGroup.add(sphere);
});

const connections = [[0, 1], [0, 2], [0, 3], [0, 4]];
connections.forEach(([start, end]) => {
  const material = new THREE.LineBasicMaterial({ color: 0xffffff });
  const points = [
    new THREE.Vector3(...nodes[start].position),
    new THREE.Vector3(...nodes[end].position),
  ];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const line = new THREE.Line(geometry, material);
  nodeGroup.add(line);
});

const controls = new OrbitControls(camera, renderer.domElement);
const animate = () => {
  nodeGroup.rotation.y += 0.01;
  controls.update();
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};
animate();
