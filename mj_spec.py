import mujoco
import mujoco.viewer as viewer

scene_path = "scene.xml"

spec = mujoco.MjSpec()

spec.from_file(scene_path)

plugin = spec.add_plugin()
plugin.name = "mujoco.elasticity.cable"

instance = plugin.add_instance()
instance.name = "compositetip"
exit()

worldbody = spec.worldbody

guidewire_body = worldbody.add_body()
guidewire_body.name = "tip"
guidewire_body.pos = [0.01, -0.5, 0.002]
guidewire_body.quat = [0.707107, 0, 0, 0.707107]


def create_nested_body(parent_body, index, rgba):
    body = parent_body.add_body()
    body.name = f"tipB_{index}"

    geom = body.add_geom()
    geom.name = f"tipG{index}"
    geom.size = [0.00089, 0.003, 0]
    geom.pos = [0.003, 0, 0]
    geom.quat = [0.707107, 0, -0.707107, 0]
    geom.type = mujoco.mjtGeom.mjGEOM_CAPSULE
    geom.condim = 1
    geom.rgba = rgba

    site = body.add_site()
    site.name = f"tipS_{index}"
    site.pos = [0, 0, 0]
    site.group = 3

    plugin = body.add_plugin()
    plugin.instance = "compositetip"

    if index < 5:
        next_body = create_nested_body(
            body, index + 1, [0, 0.0842107 - index * 0.02, 1, 1]
        )
        next_body.pos = [0.006, 0, 0]
        joint = next_body.add_joint()
        joint.name = f"tipJ_{index + 1}"
        joint.pos = [0, 0, 0]
        joint.type = mujoco.mjtJoint.mjJNT_BALL
        joint.group = 3
        joint.actuatorfrclimited = False
        joint.damping = 0.001

    return body


# Create the first body and recursively add nested bodies
create_nested_body(guidewire_body, 0, [0, 0.0842107, 1, 1])

model = spec.compile()
exit()
print(spec.to_xml())
with open("test.xml", "w") as f:
    f.write(spec.to_xml())
viewer.launch(model)
