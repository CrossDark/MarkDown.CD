import setuptools

from CrossDown import Meta

meta = Meta(3, 5, 8)

setuptools.setup(
    name="CrossDown",
    version=meta.version,
    author="CrossDark",
    author_email="liuhanbo333@icloud.com",
    description="CrossDark's MarkDown",
    long_description=meta.long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CrossDark/CrossDown",
    packages=setuptools.find_packages(),
    install_requires=meta.requirements,
    package_data={
        '': ['Static/*'],  # 这将包含static文件夹下的所有子文件夹和文件
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent"
    ],
)
