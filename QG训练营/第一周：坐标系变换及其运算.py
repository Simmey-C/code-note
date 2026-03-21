import numpy as np
import json
import math

class CoordinateSystem:
    def __init__(self, axis, vectors):
        self.axis = np.array(axis, dtype = float)
        self.vectors = np.array(vectors)
        self.dimension = len(axis)

    #  向量与坐标轴的夹角
    def axis_angle(self):
        angles = []
        for vec in self.vectors:
            vec_angle = []
            vec_norm = np.linalg.norm(vec)

            if vec_norm == 0:
                for _ in self.axis:
                    vec_angle.append(0)
                angles.append(vec_angle)
                continue

            unit_vec = vec / np.linalg.norm(vec)
            for ax in self.axis:
                unit_ax = ax / np.linalg.norm(ax)
                cos_angle = np.dot(unit_ax, unit_vec)
                cos_angle = np.clip(cos_angle, -1, 1)
                angle = math.acos(cos_angle)
                vec_angle.append(angle)

            angles.append(vec_angle)
        return angles

    #  改变坐标轴
    def change_axis(self, new_axis):
        old_axis = self.axis
        new_axis = np.array(new_axis, dtype=float)

        old_basis = old_axis.T
        new_basis = new_axis.T

        try:
            new_basis_inv = np.linalg.inv(new_basis)
            # T坐标变换公式：新坐标 = 新基⁻¹ × 旧基 × 原坐标
            new_vectors = (new_basis_inv @ old_basis @ self.vectors.T)
            self.vectors = new_vectors.T
            self.axis = new_axis
            print("坐标轴已变更为：", new_axis)
        except np.linalg.LinAlgError:
            print("坐标轴变换失败，请检查输入坐标轴是否正交")
            raise

    #  计算坐标轴面积
    def axis_area(self):
        mat = self.axis
        vol = abs(np.linalg.det(mat))
        return round(vol, 4)

    #  计算坐标轴投影
    def axis_projection(self):
        projections = []
        for vec in self.vectors:
            pro = []
            for ax in self.axis:
                norm = np.linalg.norm(ax)
                unit = ax / norm
                proj = [(np.dot(vec, unit)).round(4).tolist()]
                pro.append(proj)
            projections.append(pro)
        return projections

    def get_vectors(self):
        return self.vectors

    def get_axis(self):
        return self.axis


def test_with_json_file(filename):
    print("开始测试JSON文件中的任务组")
    print(f"文件名: {filename}")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"成功读取 {len(data)} 个任务组")

        for group_idx, group in enumerate(data, 1):
            print(f"\n{'=' * 80}")
            print(f"任务组 {group_idx}: {group['group_name']}")
            print(f"{'=' * 80}")

            print(f"向量数量: {len(group['vectors'])}")
            print(f"初始坐标轴: {group['ori_axis']}")
            print(f"任务列表: {[task['type'] for task in group['tasks']]}")

            cs = CoordinateSystem(group['ori_axis'], group['vectors'])

            try:
                if cs.dimension == len(cs.axis[0]):
                    det = np.linalg.det(cs.axis)
                    if abs(det) > 1e-10:
                        print(f"成功建立初始坐标系")
                    else:
                        print(f"建立初始坐标系失败")
            except:
                print(" 无法计算行列式，可能是非方阵坐标系")

            for task_idx, task in enumerate(group['tasks'], 1):
                task_type = task['type']
                print(f"\n--- 任务 {task_idx}: {task_type} ---")

                try:
                    if task_type == 'axis_angle':
                        result = cs.axis_angle()
                        print(f"计算结果（向量与各轴的夹角，单位：弧度）:")
                        for i in result:
                            print(i)

                    elif task_type == 'axis_projection':
                        result = cs.axis_projection()
                        print(f"计算结果（向量在各轴上的投影长度）:")
                        for i in result:
                            print(i)

                    elif task_type == 'area':
                        result = cs.axis_area()
                        if cs.dimension == 2:
                            print(f"坐标系面积缩放倍数: {result}")
                        elif cs.dimension == 3:
                            print(f"坐标系体积缩放倍数: {result}")
                        else:
                            print(f"坐标系{cs.dimension}维体积缩放倍数: {result}")

                    elif task_type == 'change_axis':
                        new_axis = task['obj_axis']
                        print(f"新坐标轴: {new_axis}")

                        try:
                            new_axis_array = np.array(new_axis)
                            if len(new_axis_array) == len(new_axis_array[0]):
                                new_det = np.linalg.det(new_axis_array)
                                if abs(new_det) > 1e-10:
                                    print(f"成功建立新坐标系")
                                else:
                                    print(f"建立新坐标系失败")
                        except:
                            pass

                        cs.change_axis(new_axis)
                        print(f"转移后的向量: {cs.get_vectors()}")

                except Exception as e:
                    print(f"任务执行失败: {e}")

        print(f"\n{'=' * 80}")
        print("所有任务组测试完成！")
        print(f"{'=' * 80}")

    except FileNotFoundError:
        print(f"\n✗ 错误: 找不到文件 '{filename}'")

    except json.JSONDecodeError as e:
        print(f"\n✗ 错误: JSON文件格式错误 - {e}")

    except Exception as e:
        print(f"\n✗ 其他错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    json_filename = "../QG训练营/data(1).json"
    test_with_json_file(json_filename)
    print("\n" + "=" * 80)
    print("程序执行完毕")
    print("=" * 80)

